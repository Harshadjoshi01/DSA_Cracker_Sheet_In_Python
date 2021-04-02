#include<iostream>
using namespace std;

int main(){
    int test_case = 0;
    cin>>test_case;
    while(test_case){
        int n;
        long long int k, d;
        cin>>n>>k>>d;
        long long int setter_questions[n];
        long long int total_questions = 0;
        long long int total_no_contests = 0;
        long long int total_questions_expected = k * d;
        for (int i = 0; i < n; i++){
            cin>>setter_questions[i];
            total_questions += setter_questions[i];
        }
        if (total_questions < k){
            cout<<0<<endl;
        }
        else if (total_questions >= total_questions_expected){
            cout<<d<<endl;
        }
        else{
            total_no_contests = total_questions/k;
            cout<<total_no_contests<<endl;
        }

        test_case -= 1;

    }
    
    return 0;

}