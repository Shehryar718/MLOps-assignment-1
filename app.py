from flask import Flask, jsonify
import torch
from torchvision.datasets import MNIST
from torchvision import transforms
from torch.utils.data import DataLoader
from train import OCRModel

app = Flask(__name__)

def get_test_accuracy():
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    test_dataset = MNIST(root='./data', download=True, train=False, transform=transform)
    test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

    model = OCRModel()
    model.load_state_dict(torch.load('models/ocr_model.pth'))
    model.eval()

    correct = 0
    total = 0

    with torch.no_grad():
        for data, target in test_loader:
            output = model(data)
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
            total += target.size(0)

    accuracy = 100.0 * correct / total
    return accuracy

@app.route('/accuracy', methods=['GET'])
def accuracy():
    accuracy_value = get_test_accuracy()
    return jsonify({"accuracy": accuracy_value})

if __name__ == '__main__':
    app.run(debug=True)

