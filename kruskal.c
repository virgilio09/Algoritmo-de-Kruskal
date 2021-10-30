#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int nro_vertices;
    int grau_max;
    int** arestas;
    float** pesos;
    int* grau;

}Grafo;   

Grafo* cria_grafo(int nro_vertices, int grau_max){
    Grafo *gr = (Grafo*) malloc(sizeof(Grafo));

    gr->nro_vertices = nro_vertices;
    gr->grau_max = grau_max;
    gr->grau = (int*) calloc(nro_vertices, sizeof(nro_vertices));
    gr->arestas = (int**) malloc(nro_vertices*sizeof(int*));
    gr->pesos = (float**) malloc(grau_max*sizeof(float*));

    for(int i=0; i<nro_vertices; i++){
        gr->arestas[i] = (int*) malloc(grau_max*sizeof(int));
        gr->pesos[i] = (float*) malloc(grau_max*sizeof(float));
    }
    return gr;
}

int insereAresta(Grafo* gr, int orig, int dest, int eh_digrafo, float peso){


    if(gr == NULL)
        return  0;
    if(orig < 0 || orig >= gr->nro_vertices)
        return  0;
    if(dest < 0 || dest >= gr->nro_vertices)
        return  0;

    gr->arestas[orig][gr->grau[orig]] = dest;
    gr->pesos[orig][gr->grau[orig]] = peso;

    gr->grau[orig]++;

    if(eh_digrafo == 0)
        insereAresta(gr, dest, orig, 1, peso);
    
    return 1;
}

void libera_grafo(Grafo* gr){

    if(gr != NULL){
        
        for(int i=0; i<gr->nro_vertices; i++){
            free(gr->arestas[i]);
            free(gr->pesos[i]);
        }
        free(gr->arestas);
        free(gr->pesos);
        free(gr->grau);
        free(gr);

    }
}

void algKruskal(Grafo *gr, int oring, int *pai){
    int dest, primeiro, NV = gr->nro_vertices;
    double menorPeso;
    int *arv = (int*) malloc(NV * sizeof(int));

    for(int i=0; i < NV; i++){
        arv[i] = i;
        pai[i] = -1; // sem pai
    }
    pai[oring] = oring;

    while (1){
        primeiro = 1;
        for(int i=0; i < NV; i++){
            for(int j=0; j < gr->grau[i]; i++){
                //   procurando o menor peso
                if(arv[i] != arv[gr->arestas[i][j]]){
                    if(primeiro){
                        menorPeso = gr->pesos[i][j];
                        oring = i;
                        dest = gr->arestas[i][j];
                        primeiro = 0;
                    }else{
                        if(menorPeso > gr->pesos[i][j]){
                            menorPeso = gr->pesos[i][j];
                            oring = i;
                            dest = gr->arestas[i][j];
                        }
                    }
                }

            }
        }
        if(primeiro == 1) break;
        if(pai[oring] == -1) pai[oring] = dest;
        else pai[dest] = oring;

        for(int i=0; i < NV; i++){
            if(arv[i] == arv[dest])
                arv[i] = arv[oring]; 
        }
    }
    
}
int main(){

    Grafo *gr;
    gr = cria_grafo(10, 7);

    insereAresta(gr, 0, 1, 0, 6);

    int pai[6];
    
    for(int i; i<6; i++)
        printf("%d: %d\n", pai[i], i);
    
    libera_grafo(gr);
    return 0;
}