import tensorflow as tf 
import matplotlib.pyplot as plt  ## 이미지를 그리는 라이브러리
# from ImageClassifier import ImageClassifier ## 일단 주석 처리해 둠. 
# ImageClassifier class만들고 나서 주석 해제
def run_classifier():
    fashion_mnist = tf.keras.datasets.fashion_mnist 
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data() 
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    print("Train data shape") 
    print(train_images.shape) 
    print("Train data labels") 
    print(train_labels)
    print("Test data shape") 
    print(test_images.shape) 
    print("Test data labels") 
    print(test_labels)

    ##### def run_classifier() 내용 이어서.
    plt.figure() 
    plt.imshow(train_images[0]) 
    plt.colorbar()
    plt.grid(False) 
    plt.show()

    train_images = train_images / 255.0 
    test_images = test_images / 255.0

    plt.figure(figsize=(10,10)) 
    for i in range(25):
        plt.subplot(5,5,i+1) 
        plt.xticks([])
        plt.yticks([]) 
        plt.grid(False) 
        plt.imshow(train_images[i], cmap=plt.cm.binary) 
        plt.xlabel(class_names[train_labels[i]])
    plt.show()

##### classifier train and predict – begin
##ImageClassifier class와 함께
##우리가 만들어야 할 부분
##### classifier train and predict – end ##### def run_classifier() 끝
if __name__ == "__main__":
# execute only if run as a script 
    run_classifier()