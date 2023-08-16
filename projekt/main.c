#include <stdlib.h>
#include <stdio.h>

#define board_(i,j) board[(i)*m+(j)]
#define result_(i,j) result[(i)*m+(j)]
#define get_(i,j) ((i)>=0&&(i)<n&&(j)>=0&&(j)<m&&result_(i,j)?1:0)

int m, n;
int *board;
int *result;

int print_path(){
//    for(int i = 0; i < n; i++) {
//
//        for(int j = 0; j < m; j++) {
//            printf("%d",result_(i,j));
//        }
//        printf("\n");
//    }
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
        if (i<0||i>n||j<0||j>m) return 0;
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


int get_input(){
    scanf("%d %d", &m, &n);
    board = malloc(sizeof(int)*(2*n*m+1));
    result = board + n*m;
    char *txt = malloc (sizeof(char)*(m+1));
    for(int i = 0; i < n; i++) {
        scanf("%s",txt);
        for(int j = 0; j < m; j++) {
            board_(i,j) = txt[j]-48;
            result_(i,j) = 0;
        }
    }
    free(txt);
    return 0;
}

int free_all(){
    free(board);
    return 0;
}

int rek(int i,int j, int val){
    if(i < 0 || i >= n || j < 0 || j > m) return 0;
    int u;
    if(get_(i-1,j) == val) u=0;
    else u=1;
    if(i>0 && board_(i-1,j) != u) return 0;

    int l;
    if(get_(i,j-1) == val) l=0;
    else l=1;
    if( j>0 && ((board_(i,j-1) < l) || (i == n-1 && board_(i,j-1) != l))) return 0;

    int x=0;
    if(val == 1 && i == n-1) x++;
    if(val == 1 && j == m-1) x++;
    if(l+u+x > board_(i,j)) return 0;

    if(i>0) board_(i-1,j)-=u;
    if(j>0) board_(i,j-1)-=l;
    board_(i,j) -= (l+u+x);

    result_(i,j) = val;
    if(i == n-1 && j == m-1 ) return 1;

    if(j < m-1){
        if(rek(i,j+1,0) || rek(i,j+1,1)) return 1;
    }else if(rek(i+1,0,0) || rek(i+1,0,1)) return 1;

    if(i>0) board_(i-1,j)+=u;
    if(j>0) board_(i,j-1)+=l;
    board_(i,j) += (l+u+x);

    return 0;
}

int main(){
    get_input();
    if (rek(0,0,0) || rek(0,0,1)) print_path();
    free_all();
    return 0;
}
