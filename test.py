import torch
from torchvision.datasets import MNIST
from torchvision import transforms
from torch.utils.data import DataLoader
import pytest
from train import OCRModel

@pytest.fixture
def test_data_loader():
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    test_dataset = MNIST(root='./data', download=True, train=False, transform=transform)
    test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)
    return test_loader

def test_accuracy(test_data_loader):
    model = OCRModel()
    model.load_state_dict(torch.load('models/ocr_model.pth'))
    model.eval()

    correct = 0
    total = 0

    with torch.no_grad():
        for data, target in test_data_loader:
            output = model(data)
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
            total += target.size(0)

    accuracy = 100.0 * correct / total

    accuracy_threshold = 95.0

    assert accuracy >= accuracy_threshold, f"Accuracy is below the expected threshold ({accuracy_threshold}%)"
