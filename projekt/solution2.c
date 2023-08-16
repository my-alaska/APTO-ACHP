#include <stdlib.h>
#include <stdio.h>

#define board_(i,j) board[(i)*m+(j)]
#define result_(i,j) result[(i)*m+(j)]
#define get_(i,j) ((i)>=0&&(i)<n&&(j)>=0&&(j)<m&&result_(i,j)==1?1:0)

int m, n, idx;
int *board;
int *result;
int *stack;

int get_input(){
    scanf("%d %d", &m, &n);
    board = malloc(sizeof(int)*n*m);
    char *txt = malloc (sizeof(char)*m);
    for(int i =0; i < n; i++) {
        scanf("%s",txt);
        for(int j = 0; j < m; j++) board[j+m*i] = txt[j]-48;
    }
    free(txt);
    result = malloc(sizeof(int)*n*m);
    stack = malloc(sizeof(int)*n*m);
    for(int i = 0 ; i < m*n; i++) result[i]=0;
//    printf("input ok\n");
    return 0;
}

void free_all(){
    free(board);
    free(result);
    free(stack);
}

int print_path(){
    int i_=0, j_=0;
    while (get_(i_,j_) == 0){
        j_++;
        if (m == j_){j_ = 0;i_++;}
    }
    printf("%d %d\n", j_, i_);
    register int i = i_;
    register int j = j_;
    register char prev = '_';
    do{
        switch(prev){
            case 'R':
                if(get_(i-1,j)){i-=1;prev = 'U';}
                else if(get_(i,j))j+=1;
                else{i+=1;prev = 'D';}
                break;
            case 'D':
                if(get_(i,j)){j+=1;prev = 'R';}
                else if(get_(i,j-1)) i+=1;
                else{j-=1;prev = 'L';}
                break;
            case 'L':
                if(get_(i,j-1)){i+=1; prev = 'D';}
                else if(get_(i-1,j-1)) j-=1;
                else{i-=1;prev = 'U';}
                break;
            case 'U':
                if(get_(i-1,j-1)){j-=1;prev='L';}
                else if(get_(i-1,j)) i-=1;
                else{j+=1;prev = 'R';}
                break;
            default:
                prev = 'R';
                j+=1;
                break;
        }
        printf("%c",prev);
    }while(i!=i_ || j!=j_);
    return 0;
}

int check_solution(){
    int * row = board;
    int neighbours;
    register int i,j;
    for(i = 0; i < n; i++){
        for(j = 0; j < m; j++){
            neighbours = get_(i-1,j) + get_(i+1,j) + get_(i,j-1) + get_(i,j+1);
            neighbours = get_(i,j) ? 4 - neighbours : neighbours;
            if (neighbours != row[j]) return 0;
        }
        row+=m;
    }
    return 1;
}

void print_result(int a, int b){
    printf("%d %d\n",a,b);
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            printf("%d",result_(i,j));
        }
        printf("\n");
    }
    printf("\n");
}

//    1
// 4     2
//    3

int get_rek(int i, int j){
//    print_result(i,j);


    if(idx >= m*n || result_(i,j) == 1 || board_(i,j) < 2) return 0;
    if(i > 0 && result_(i-1,j) && stack[idx] != 3) return 0;
    if(j > 0 && result_(i,j-1) && stack[idx] != 2) return 0;
    if(i < n-1 && result_(i+1,j) && stack[idx] != 1) return 0;
    if(j < m-1 && result_(i,j+1) && stack[idx] != 4) return 0;

    if(i > 0   && j > 0   && result_(i-1,j-1) && stack[idx] != 3 && stack[idx] != 2) return 0;
    if(i < n-1 && j > 0   && result_(i+1,j-1) && stack[idx] != 1 && stack[idx] != 2) return 0;
    if(i > 0   && j < m-1 && result_(i-1,j+1) && stack[idx] != 3 && stack[idx] != 4) return 0;
    if(i < n-1 && j < m-1 && result_(i+1,j+1) && stack[idx] != 1 && stack[idx] != 4) return 0;

    if(j > 0 && result_(i,j-1) && stack[idx] != 2) return 0;
    if(i < n-1 && result_(i+1,j) && stack[idx] != 1) return 0;
    if(j < m-1 && result_(i,j+1) && stack[idx] != 4) return 0;


    idx++;
    result_(i,j) = 1;
    if(board_(i,j) == 3) {
        if(check_solution()) return 1;
        else{
            idx--;
            result_(i,j) = 0;
            return 0;
        }
    }
//    print_result(i,j);


    stack[idx] = 1;
    if(i > 0 && get_rek(i-1,j)) return 1;
    stack[idx] = 4;
    if(j > 0 && get_rek(i,j-1)) return 1;
    stack[idx] = 3;
    if(i < n-1 && get_rek(i+1,j)) return 1;
    stack[idx] = 2;
    if(j < m-1 && get_rek(i,j+1)) return 1;

    result_(i,j) = 0;
    idx--;
    return 0;
}

int get_path(int i, int j){
    idx = 0;

    result_(i,j) = 1;

    if(i > 0)   {
        stack[idx] = 1;
        if(get_rek(i-1,j)) return 1;
    }
    if(j > 0)   {
        stack[idx] = 4;
        if(get_rek(i,j-1))return 1;
    }
    if(i < n-1) {
        stack[idx] = 3;
        if(get_rek(i+1,j))return 1;
    }
    if(j < m-1) {
        stack[idx] = 2;
        if(get_rek(i,j+1)) return 1;
    }

    result_(i,j) = 0;
    return 0;
}

int main(){
    get_input();

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++){
            if (board_(i,j) == 3 && get_path(i,j)){
                print_path();
            }
        }
    }

    free_all();
    return 0;
}

//11 10
//22222222222
//23222322232
//22222222222
//22222222222
//22222222222
//22222222222
//22222222222
//22222222222
//22232223222
//32222222223


