// C or C++ program for insertion and 
// deletion in Circular Queue 
#include<bits/stdc++.h> 
using namespace std; 
  
struct Queue 
{ 
    // Initialize front and rear 
    int rear, front; 
  
    // Circular Queue 
    int size; 
    int *arr; 
  
    Queue(int s) 
    { 
       front = rear = -1; 
       size = s; 
       arr = new int[s]; 
    } 
  
    void enQueue(int value); 
    int deQueue(); 
    void displayQueue(); 
    bool isEmpty();
}; 
  
  
/* Function to create Circular queue */
void Queue::enQueue(int value) 
{ 
    if ((front == 0 && rear == size-1) || 
            (rear == (front-1)%(size-1))) 
    { 
        printf("\nQueue is Full"); 
        return; 
    } 
  
    else if (front == -1) /* Insert First Element */
    { 
        front = rear = 0; 
        arr[rear] = value; 
    } 
  
    else if (rear == size-1 && front != 0) 
    { 
        rear = 0; 
        arr[rear] = value; 
    } 
  
    else
    { 
        rear++; 
        arr[rear] = value; 
    } 
} 
  
// Function to delete element from Circular Queue 
int Queue::deQueue() 
{ 
    if (front == -1) 
    { 
        printf("\nQueue is Empty"); 
        return INT_MIN; 
    } 
  
    int data = arr[front]; 
    arr[front] = -1; 
    if (front == rear) 
    { 
        front = -1; 
        rear = -1; 
    } 
    else if (front == size-1) 
        front = 0; 
    else
        front++; 
  
    return data; 
} 
  
// Function displaying the elements 
// of Circular Queue 
void Queue::displayQueue() 
{ 
    if (front == -1) 
    { 
        printf("\nQueue is Empty"); 
        return; 
    } 
    printf("\nElements in Circular Queue are: "); 
    if (rear >= front) 
    { 
        for (int i = front; i <= rear; i++) 
            printf("%d ",arr[i]); 
    } 
    else
    { 
        for (int i = front; i < size; i++) 
            printf("%d ", arr[i]); 
  
        for (int i = 0; i <= rear; i++) 
            printf("%d ", arr[i]); 
    } 
    printf("\n");
}
bool Queue::isEmpty(){
    bool empty = false;
    if(front == -1){
        empty = true;
    }
    return empty; 
}
void choices(){
    printf("\n");
    cout<<"Which operation you want to perform: "<<endl;

    cout<<"Press 1 for Insert an element "<<endl;

    cout<<"Press 2 for Dequeue(Delete) an element "<<endl;

    cout<<"Press 3 for Display the queue "<<endl;

    cout<<"Press 4 to end the program "<<endl;
}
/* Driver of the program */
int main() 
{ 
    int size;
    cout<<"How many elements you have to insert in Circular Queue: "<<endl;
    cin>>size;
    Queue q(size);
    int end_program = 0;
    while(end_program != 4){
        choices();
        int choice;
        cin>>choice;
        switch (choice)
        {
            case 1 :
                int x;
                cout<<"Put the element: ";
                cin>>x;
                q.enQueue(x);
                break;
            case 2:
                if (q.isEmpty()){
                    cout<<"Queue is Empty"<<endl;
                }else{
                    q.deQueue();
                    cout<<"First element is deleted"<<endl;
                }
                break;
            case 3:
                q.displayQueue();
                break;
            case 4:
                cout<<"***************Programe is ended******************"<<endl;
                end_program = 4;
                break;
            default:
                cout<<"*********Please Provide the right Choice**********"<<endl;
                break;
        }
    }
    return 0; 
} 