#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <cstring>

void merge(std::vector<int>& arr, int left, int mid, int right) {
int n1 = mid - left + 1;
int n2 = right - mid;


std::vector<int> L(n1), R(n2);

for (int i = 0; i < n1; i++)
    L[i] = arr[left + i];
for (int j = 0; j < n2; j++)
    R[j] = arr[mid + 1 + j];

int i = 0, j = 0, k = left;
while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
        arr[k] = L[i];
        i++;
    } else {
        arr[k] = R[j];
        j++;
    }
    k++;
}

while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
}

while (j < n2) {
    arr[k] = R[j];
    j++;
    k++;
}
}

void mergeSort(std::vector<int>& arr, int left, int right) {
if (left < right) {
int mid = left + (right - left) / 2;


    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}
}

int main() {
std::ifstream inputFile("inupt_sort.txt");
if (!inputFile) {
std::cerr << "input 파일을 열 수 없습니다." << strerror(errno) << std::endl;
return 1;
}


// 숫자를 저장할 벡터 선언
std::vector<int> numbers;
int number;


while (inputFile >> number) {
    numbers.push_back(number);
}
inputFile.close();


auto start = std::chrono::high_resolution_clock::now();

// 병합 정렬 수행
mergeSort(numbers, 0, numbers.size() - 1);


auto end = std::chrono::high_resolution_clock::now();


std::ofstream outputFile("output_merge_sort.txt");
for (const int& num : numbers) {
    outputFile << num << std::endl; // 각 숫자를 새 줄에 작성
}
outputFile.close();


std::chrono::duration<double> elapsed = end - start;
std::cout << "정렬 완료! 소요 시간: " << elapsed.count() << "초" << std::endl;

return 0; 
}
