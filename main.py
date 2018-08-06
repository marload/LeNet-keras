from data import DATA
from lenet import LeNet
from plot import plot_loss
import matplotlib.pyplot as plt

def main():
    batch_size = 128
    epoch = 15

    data = DATA()
    model = LeNet(data.input_shape, data.num_classes)

    hist = model.fit(data.x_train, data.y_train, batch_size=batch_size, epochs=epoch, validation_split=0.2)
    score = model.evaluate(data.x_test, data.y_test, batch_size=batch_size)

    print()
    print('Test Loss= ', score)

    plot_loss(hist)
    plt.show()

if __name__ == '__main__':
    main()