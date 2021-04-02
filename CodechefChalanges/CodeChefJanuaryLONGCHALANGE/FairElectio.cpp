#include<iostream>
#include<algorithm>
using namespace std;

int sumArray(int arr[], int size){
    int sum = 0;
    for(int i = 0; i < size; i++){
        sum += arr[i]; 
    }
    return sum;
}
int main (){
    int test_case = 0;
    cin>> test_case;
    while(test_case){
        int n,m;
        cin>>n>>m;
        int arr_john[n];
        int arr_jackson[m];
        for(int i = 0; i < n; i++){
            cin>>arr_john[i];
        }
        for(int i = 0; i < m; i++){
            cin>>arr_jackson[i];
        }
        sort(arr_john, arr_john+n);
        sort(arr_jackson, arr_jackson+m);
        int sum_votes_john = sumArray(arr_john,n);
        int sum_votes_jackson = sumArray(arr_jackson,m);
        int min_swaps = 0;
        int max_swaps = min(n,m);
        int idx_jackson = m-1;
        int idx_john = n-1;
        int swaping_idx = 0;

        while((sum_votes_john <= sum_votes_jackson) && (min_swaps <= max_swaps)){
            if ((arr_john[idx_john] < arr_jackson[idx_jackson]) && (swaping_idx <= idx_john ) && (idx_jackson>=0) && (idx_john >= 0) && (swaping_idx >= n-1) ){
                int temp = arr_jackson[idx_jackson];
                arr_jackson[idx_jackson] = arr_john[swaping_idx];
                arr_john[swaping_idx] = temp;
                min_swaps++;
                swaping_idx++;
                idx_jackson--;
                sum_votes_john = sumArray(arr_john,n);
                sum_votes_jackson = sumArray(arr_jackson,m);

            }
            else if (idx_john >= 0){
                idx_john--;
            }
            

        }
        if (sum_votes_john <= sum_votes_jackson) {
            cout<<-1<<endl;
        }
        else{
            cout<<min_swaps<<endl;
        }
        

        test_case--;
    }
    return 0; 
}