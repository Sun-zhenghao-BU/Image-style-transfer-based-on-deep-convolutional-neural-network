import torch
import torchvision
from torchvision import transforms, models
from PIL import Image
import matplotlib.pyplot as plt
from torch.autograd import Variable
import copy
import GUI_FirstWin
import GUI_AlertWin

'''
import GUI_ResultShowWin

Show_Win = GUI_ResultShowWin.ResultShowWin()
这两句话导致QWidget: Must construct a QApplication before a QWidget问题！

'''
# matplotlib inline
# loading image
transform = transforms.Compose([transforms.Resize([224, 224]),
                                transforms.ToTensor()])
ToPIL = torchvision.transforms.ToPILImage()

n_epoch = 20
run = [0]
stylelint = []
contentlint = []
Totallint = []
Epoch = []


def loadimg(path=None):
    img = Image.open(path)
    img = transform(img)
    img = img.unsqueeze(0)
    return img


def img_show(img, title=None):
    img = img.clone().cpu()
    img = img.view(3, 224, 224)
    img = ToPIL(img)

    if title is not None:
        plt.title(title)
    plt.imshow(img)


# define content loss function and style loss function
class Content_loss(torch.nn.Module):
    def __init__(self, weight, target):
        super(Content_loss, self).__init__()
        self.weight = weight
        self.target = target.detach() * weight
        self.loss_fn = torch.nn.MSELoss()

    def forward(self, input):
        self.loss = self.loss_fn(input * self.weight, self.target)
        self.output = input
        return self.output

    def backward(self):
        self.loss.backward(retain_graph=True)
        return self.loss


class gram_matrix(torch.nn.Module):
    def forward(self, input):
        a, b, c, d = input.size()
        feature = input.view(a * b, c * d)
        gram = torch.mm(feature, feature.t())
        return gram.div(a * b * c * d)


class Style_loss(torch.nn.Module):
    def __init__(self, weight, target):
        super(Style_loss, self).__init__()
        self.weight = weight
        self.target = target.detach() * weight
        self.loss_fn = torch.nn.MSELoss()
        self.gram = gram_matrix()

    def forward(self, input):
        self.output = input.clone()
        self.G = self.gram(input)
        self.G.mul_(self.weight)
        self.loss = self.loss_fn(self.G, self.target)
        return self.output

    def backward(self):
        self.loss.backward(retain_graph=True)
        return self.loss


def output():
    # define the parameters which need to be optimized and transfer the model
    # star_time = time.time()
    AW = GUI_AlertWin.AlertWin()
    if GUI_FirstWin.content_image_address() is None or GUI_FirstWin.style_image_address() is None:
        AW.show()
    else:
        content_img = loadimg(GUI_FirstWin.content_image_address())
        content_img = Variable(content_img).cpu()
        style_img = loadimg(GUI_FirstWin.style_image_address())
        style_img = Variable(style_img).cpu()
        print(content_img.size())

    use_gpu = torch.cuda.is_available()
    cnn = models.vgg16(pretrained=True).features
    if use_gpu:
        cnn = cnn.cuda()
    print(cnn)

    content_layer = ["Conv_5", "Conv_6"]
    style_layer = ["Conv_1", "Conv_2", "Conv_3", "Conv_4", "Conv_5"]

    content_losses = []
    style_losses = []

    content_weight = 0.1
    style_weight = 1000

    new_model = torch.nn.Sequential()
    model = copy.deepcopy(cnn)
    gram = gram_matrix()

    if use_gpu:
        new_model = new_model.cuda()
        gram = gram.cuda()

    index = 1
    for layer in list(model):
        if isinstance(layer, torch.nn.Conv2d):
            name = "Conv_" + str(index)
            new_model.add_module(name, layer)
            if name in content_layer:
                target = new_model(content_img).clone()
                content_loss = Content_loss(content_weight, target)
                new_model.add_module("content_loss_" + str(index), content_loss)
                content_losses.append(content_loss)

            if name in style_layer:
                target = new_model(style_img).clone()
                target = gram(target)
                style_loss = Style_loss(style_weight, target)
                new_model.add_module("style_loss_" + str(index), style_loss)
                style_losses.append(style_loss)

        if isinstance(layer, torch.nn.ReLU):
            name = "Relu_" + str(index)
            new_model.add_module(name, layer)
            index = index + 1

        if isinstance(layer, torch.nn.MaxPool2d):
            name = "MaxPool_" + str(index)
            new_model.add_module(name, layer)

    print(new_model)

    input_img = content_img.clone()
    parameter = torch.nn.Parameter(input_img.data)
    optimizer = torch.optim.LBFGS([parameter])

    def closure():
        optimizer.zero_grad()
        style_score = 0
        content_score = 0
        parameter.data.clamp_(0, 1)
        new_model(parameter)
        for sl in style_losses:
            style_score += sl.backward()

        for cl in content_losses:
            content_score += cl.backward()

        run[0] += 1
        if run[0] % 10 == 0:
            print('Epoch : {} Style Loss : {:4f} Content Loss: {:4f}'.format(run[0], style_score.item(),
                                                                             content_score.item()))
            stylelint.append(style_score.item())
            contentlint.append(content_score.item())
            Totallint.append(style_score.item() + content_score.item())
            Epoch.append(run[0])
        return style_score + content_score

    while run[0] < n_epoch:
        optimizer.step(closure)

    return parameter.data


def loss_figure_output():
    global run, stylelint, contentlint, Totallint, Epoch
    plt.figure()
    x = range(len(Epoch))
    plt.plot(stylelint, marker='D', color='b', label='Style_loss')
    plt.plot(contentlint, marker='*', color='r', label='Content_loss')
    plt.plot(Totallint, marker='^', color='g', label='Total_loss')
    plt.xticks(x, Epoch)
    plt.ylabel('loss_value')
    plt.xlabel('epoch_num')
    plt.title('Loss Value Graph')
    plt.legend()
    plt.savefig("./result_figure/loss_figure.jpg")
    run = [0]
    stylelint = []
    contentlint = []
    Totallint = []
    Epoch = []






