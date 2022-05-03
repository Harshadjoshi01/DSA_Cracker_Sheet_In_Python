#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    int arr[n];
    cin>>arr[0];
    int maximum = arr[0];
    int minimum = arr[0];
    for (int i = 1; i < n; i++){
        cin>>arr[i];
        if (arr[i] > maximum){
            maximum = arr[i];
        }
        if (arr[i] < minimum){
            minimum = arr[i];
        }
    }
    cout<<"Maximum is "<<maximum<<endl;
    cout<<"Minimum is "<<minimum<<endl;
    return 0;
    
    

}