from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        lista_vertices = set()
        lista_fim = set()
        nao_adjacentes = set()
        for v in self.vertices:
            lista_vertices.add(v.rotulo)

        for v in self.vertices:
            arestas_conectadas: set[str] = set()
            arestas_conectadas.add(v.rotulo)
            for a in self.arestas.values():
                if a.v1 == v:
                    arestas_conectadas.add(a.v2.rotulo)
                elif a.v2 == v:
                    arestas_conectadas.add(a.v1.rotulo)
            nao_adjacentes = lista_vertices - arestas_conectadas
            for v_nao_adjacentes in nao_adjacentes:
                par_v = f'{v.rotulo}-{v_nao_adjacentes}'
                if par_v[::-1] not in lista_fim:
                    lista_fim.add(par_v)

        return lista_fim
    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.arestas:
            if self.arestas[a].v1 == self.arestas[a].v2:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        grau = 0
        for a in self.arestas.values():
            if a.v1.rotulo == V:
                grau += 1
            if a.v2.rotulo == V:
                grau += 1
        return grau
    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        lista_v1 = []
        lista_v2 = []
        for a in self.arestas.values():
            lista_v1.append(a.v1)
        for b in self.arestas.values():
            lista_v2.append(b.v2)
        len_v1 = len(lista_v1)
        len_v2 = len(lista_v2)

        for i in range(len_v1):
            for j in range(len_v2):
                if i == j:
                    continue
                elif lista_v1[i] == lista_v1[j] and lista_v2[i] == lista_v2[j]:
                    return True
                elif lista_v1[i] == lista_v2[j] and lista_v2[i] == lista_v1[j]:
                    return True
        return False
    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        lista_arestas = set()
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        for i in self.arestas.values():
            if i.v1.rotulo == V or i.v2.rotulo == V:
                lista_arestas.add(i.rotulo)
        return lista_arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco() or self.ha_paralelas():
            return False

        qtd_v = len(self.vertices)
        if qtd_v > 1 and len(self.arestas) == 0:
            return False
        for a in self.arestas:
            if (self.grau(self.arestas[a].v1.rotulo) != qtd_v - 1) or (self.grau(self.arestas[a].v2.rotulo) != qtd_v - 1):
                return False
        return True

    def dfs(self, V=''):
        novo_grafo = MeuGrafo()  # Retorno do Novo Grafo

        if self.ha_laco():
            return False
        if not self.existe_rotulo_vertice(V):  # Verificação da raiz
            raise VerticeInvalidoError
        novo_grafo.adiciona_vertice(V)

        def percorre_grafo(raiz):
            arestas_vertices: str = sorted(list(self.arestas_sobre_vertice(raiz)))  # Arestas incidentes da atual raiz

            for a in arestas_vertices:
                v_1 = str(self.arestas[a].v1)
                v_2 = str(self.arestas[a].v2)

                if novo_grafo.existe_rotulo_vertice(v_1) and novo_grafo.existe_rotulo_vertice(v_2):
                    continue

                prox = v_1 if v_1 != raiz else v_2
                novo_grafo.adiciona_vertice(prox)
                novo_grafo.adiciona_aresta(self.arestas[a])
                percorre_grafo(prox)

        percorre_grafo(V)

        if len(self.vertices) != len(novo_grafo.vertices):
            return False

        print(novo_grafo)
        return novo_grafo

    def bfs(self, V=''):
        novo_grafo = MeuGrafo()

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        if self.ha_laco():
            raise ValueError

        novo_grafo.adiciona_vertice(V)
        prox_v: str = list()

        prox_v.append(V)
        while prox_v:
            vert_atual = prox_v.pop(0)
            arestas_vertices: str = sorted(list(self.arestas_sobre_vertice(vert_atual)))

            for a in arestas_vertices:
                v_1 = str(self.arestas[a].v1)
                v_2 = str(self.arestas[a].v2)

                if novo_grafo.existe_rotulo_vertice(v_1) and novo_grafo.existe_rotulo_vertice(v_2):
                    continue

                prox = v_1 if v_1 != vert_atual else v_2
                novo_grafo.adiciona_vertice(prox)
                novo_grafo.adiciona_aresta(self.arestas[a])
                prox_v.append(prox)

        if len(self.vertices) != len(novo_grafo.vertices):
            raise ValueError

        return novo_grafo








