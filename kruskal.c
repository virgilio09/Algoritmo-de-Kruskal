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

int main(){

    return 0;
}

int insereAresta(Grafo* gr, int orig, int dest, int eh_digrafo, float peso){

    int verifica = 1;

    if(gr == NULL)
        verifica = 0;
    if(orig < 0 || orig >= gr->nro_vertices)
        verifica = 0;
    if(dest < 0 || dest >= gr->nro_vertices)
        verifica = 0;

    gr->arestas[orig][gr->grau[orig]] = dest;
    gr->pesos[orig][gr->grau[orig]] = peso;

    gr->grau[orig]++;
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