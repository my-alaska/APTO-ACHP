#include <stdlib.h>
#include <stdio.h>

#define get_(i,j) ((i)>=0&&(i)<n&&(j)>=0&&(j)<m&&solution&1<<((i)*m+(j))?1:0)

unsigned int m, n;
unsigned int *board;

int get_input(){
    scanf("%d %d", &m, &n);
    board = malloc(sizeof(int)*n*m);
    char *txt = malloc (sizeof(char)*m);
    for(int i =0; i < n; i++) {
        scanf("%s",txt);
        for(int j = 0; j < m; j++) board[j+m*i] = txt[j]-48;
    }
    free(txt);
    return 0;
}

int print_path(unsigned long long solution){
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

int check_solution(unsigned long long solution){
    unsigned int * row = board;
    int neighbours;
    register int i,j;
    for(i = 0; i < n; i++){
        for(j = 0; j < m; j++){
            neighbours = get_(i-1,j) + get_(i+1,j) + get_(i,j-1) + get_(i,j+1);
            neighbours = solution & 1 << (i*m+j) ? 4 - neighbours : neighbours;
            if (neighbours != row[j]) return 0;
        }
        row+=m;
    }
    return 1;
}

int main(){
    get_input();
    register unsigned long long i;
    for(i = 1; !( i & 1 << (m*n)) ; i++) if (check_solution(i)) {
        print_path(i);
        break;
    }
    free(board);
    return 0;
}