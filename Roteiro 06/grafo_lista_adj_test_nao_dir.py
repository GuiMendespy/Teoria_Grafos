import unittest
from atividades_grafos.gerar_grafos_teste import vertices_pb
from meu_grafo_lista_adj_nao_dir import *
import gerar_grafos_teste
from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice
from bibgrafo.grafo_errors import *
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.grafo_builder import GrafoBuilder


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = GrafoJSON.json_to_grafo('test_json/grafo_pb.json', MeuGrafo())

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = GrafoJSON.json_to_grafo('test_json/grafo_pb2.json', MeuGrafo())

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = GrafoJSON.json_to_grafo('test_json/grafo_pb3.json', MeuGrafo())

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = GrafoJSON.json_to_grafo('test_json/grafo_pb4.json', MeuGrafo())

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = GrafoBuilder().tipo(MeuGrafo()).vertices(['J', 'C', 'E']).arestas(True).build()

        self.g_c_dfs = GrafoBuilder().tipo(MeuGrafo()).vertices(["J","C","E"]).arestas(
            [Aresta('a1', vertices_pb['J'], vertices_pb['C']),
             Aresta('a3',vertices_pb['C'], vertices_pb['E'])]).build()

        self.g_c2 = GrafoBuilder().tipo(MeuGrafo()).vertices(["J","C","E","T"]).arestas(True).build()

        self.g_c2_dfs = GrafoBuilder().tipo(MeuGrafo()).vertices(["J","C","E","T"]).arestas(
            [Aresta('a1', vertices_pb['J'], vertices_pb['C']),
             Aresta('a4',vertices_pb['C'], vertices_pb['E']),
             Aresta('a6',vertices_pb['E'], vertices_pb['T'])]).build()

        self.g_c3 = GrafoBuilder().tipo(MeuGrafo()).vertices(["J","C","E","T","P"]).arestas(True).build()

        self.g_c3_dfs = GrafoBuilder().tipo(MeuGrafo()).vertices(["J", "C", "E", "T","P"]).arestas(
            [Aresta('a1', vertices_pb['J'], vertices_pb['C']),
             Aresta('a5', vertices_pb['C'], vertices_pb['E']),
             Aresta('a8', vertices_pb['E'], vertices_pb['T']),
             Aresta('a10', vertices_pb['T'],vertices_pb['P'])]).build()

        lista_aresta = [Aresta('a1',Vertice('C'),Vertice('J')),
                Aresta('a2',Vertice('J'),Vertice('E')),
                Aresta('a3',Vertice('C'),Vertice('T')),
                Aresta('a4',Vertice('C'),Vertice('P'))]
        self.g_c4 = grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(["J","C","E","T","P"]).arestas(lista_aresta).build()

        self.g_c4_dfs = GrafoBuilder().tipo(MeuGrafo()).vertices(["J", "C", "E", "T","P"]).arestas(
            [Aresta('a1', vertices_pb['J'], vertices_pb['C']),
             Aresta('a3', vertices_pb['C'], vertices_pb['T']),
             Aresta('a4', vertices_pb['C'], vertices_pb['P']),
             Aresta('a2', vertices_pb['J'],vertices_pb['E'])]).build()

        self.g_c_bfs = GrafoBuilder().tipo(MeuGrafo()).vertices(["J","C","E"]).arestas(
            [Aresta('a1', vertices_pb['J'], vertices_pb['C']),
             Aresta('a2',vertices_pb['J'], vertices_pb['E'])]).build()

        self.g_c2_bfs = GrafoBuilder().tipo(MeuGrafo()).vertices(["J", "C", "E", "T"]).arestas(
            [Aresta('a1', vertices_pb['J'], vertices_pb['C']),
             Aresta('a2', vertices_pb['J'], vertices_pb['E']),
             Aresta('a3', vertices_pb['J'], vertices_pb['T'])]).build()

        self.g_c3_bfs = GrafoBuilder().tipo(MeuGrafo()).vertices(["J", "C", "E", "T", "P"]).arestas(
            [Aresta('a1', vertices_pb['J'], vertices_pb['C']),
             Aresta('a2', vertices_pb['J'], vertices_pb['E']),
             Aresta('a3', vertices_pb['J'], vertices_pb['T']),
             Aresta('a4', vertices_pb['J'], vertices_pb['P'])]).build()

        self.g_c4_bfs = GrafoBuilder().tipo(MeuGrafo()).vertices(["J", "C", "E", "T", "P"]).arestas(
            [Aresta('a1', vertices_pb['J'], vertices_pb['C']),
             Aresta('a2', vertices_pb['J'], vertices_pb['E']),
             Aresta('a3', vertices_pb['C'], vertices_pb['T']),
             Aresta('a4', vertices_pb['C'], vertices_pb['P'])]).build()

########################################################################################################################
        self.g_c5 = MeuGrafo()

        self.g_c5.adiciona_vertice('A')
        self.g_c5.adiciona_vertice('B')
        self.g_c5.adiciona_vertice('C')
        self.g_c5.adiciona_vertice('D')
        self.g_c5.adiciona_vertice('E')
        self.g_c5.adiciona_vertice('F')
        self.g_c5.adiciona_vertice('G')
        self.g_c5.adiciona_vertice('H')


        self.g_c5.adiciona_aresta('a1', 'A', 'B')
        self.g_c5.adiciona_aresta('a2', 'A', 'C')
        self.g_c5.adiciona_aresta('a3', 'B', 'E')
        self.g_c5.adiciona_aresta('a4', 'B', 'D')
        self.g_c5.adiciona_aresta('a5', 'D', 'F')
        self.g_c5.adiciona_aresta('a6', 'D', 'G')
        self.g_c5.adiciona_aresta('a7', 'D', 'H')

###############################################################################################################
        self.g_c5_dfs = MeuGrafo()

        self.g_c5_dfs.adiciona_vertice('A')
        self.g_c5_dfs.adiciona_vertice('B')
        self.g_c5_dfs.adiciona_vertice('C')
        self.g_c5_dfs.adiciona_vertice('D')
        self.g_c5_dfs.adiciona_vertice('E')
        self.g_c5_dfs.adiciona_vertice('F')
        self.g_c5_dfs.adiciona_vertice('G')
        self.g_c5_dfs.adiciona_vertice('H')


        self.g_c5_dfs.adiciona_aresta('a1', 'A', 'B')
        self.g_c5_dfs.adiciona_aresta('a3', 'B', 'E')
        self.g_c5_dfs.adiciona_aresta('a4', 'B', 'D')
        self.g_c5_dfs.adiciona_aresta('a5', 'D', 'F')
        self.g_c5_dfs.adiciona_aresta('a6', 'D', 'G')
        self.g_c5_dfs.adiciona_aresta('a7', 'D', 'H')
        self.g_c5_dfs.adiciona_aresta('a2', 'A', 'C')

####################################################################################################
        self.g_c5_bfs = MeuGrafo()

        self.g_c5_bfs.adiciona_vertice('A')
        self.g_c5_bfs.adiciona_vertice('B')
        self.g_c5_bfs.adiciona_vertice('C')
        self.g_c5_bfs.adiciona_vertice('D')
        self.g_c5_bfs.adiciona_vertice('E')
        self.g_c5_bfs.adiciona_vertice('F')
        self.g_c5_bfs.adiciona_vertice('G')
        self.g_c5_bfs.adiciona_vertice('H')

        self.g_c5_bfs.adiciona_aresta('a1', 'A', 'B')
        self.g_c5_bfs.adiciona_aresta('a2', 'A', 'C')
        self.g_c5_bfs.adiciona_aresta('a4', 'B', 'D')
        self.g_c5_bfs.adiciona_aresta('a3', 'B', 'E')
        self.g_c5_bfs.adiciona_aresta('a5', 'D', 'F')
        self.g_c5_bfs.adiciona_aresta('a6', 'D', 'G')
        self.g_c5_bfs.adiciona_aresta('a7', 'D', 'H')

#########################################################################################
        #teste ha_ciclo 1
        self.g_6 = MeuGrafo()

        self.g_6.adiciona_vertice("J")
        self.g_6.adiciona_vertice("C")
        self.g_6.adiciona_vertice("E")
        self.g_6.adiciona_vertice("P")
        self.g_6.adiciona_vertice("M")
        self.g_6.adiciona_vertice("T")
        self.g_6.adiciona_vertice("Z")

        self.g_6.adiciona_aresta("a1", "J", "T", 1)
        self.g_6.adiciona_aresta("a2", "T", "M", 1)
        self.g_6.adiciona_aresta("a3", "M", "C", 1)
        self.g_6.adiciona_aresta("a4", "C", "E", 1)
        self.g_6.adiciona_aresta("a5", "E", "P", 1)
        self.g_6.adiciona_aresta("a6", "P", "M", 1)
        self.g_6.adiciona_aresta("a7", "J", "Z", 1)

        self.lista_g_6 = ['M','a3','C','a4','E','a5','P','a6','M']

#########################################################################################
        # teste ha_ciclo 2
        self.g_7 = MeuGrafo()

        self.g_7.adiciona_vertice("J")
        self.g_7.adiciona_vertice("C")
        self.g_7.adiciona_vertice("E")
        self.g_7.adiciona_vertice("P")
        self.g_7.adiciona_vertice("M")
        self.g_7.adiciona_vertice("T")
        self.g_7.adiciona_vertice("Z")

        self.g_7.adiciona_aresta("a1", "J", "C", 1)
        self.g_7.adiciona_aresta("a2", "C", "E", 1)
        self.g_7.adiciona_aresta("a3", "E", "P", 1)
        self.g_7.adiciona_aresta("a4", "P", "M", 1)
        self.g_7.adiciona_aresta("a5", "P", "J", 1)
        self.g_7.adiciona_aresta("a6", "M", "T", 1)
        self.g_7.adiciona_aresta("a7", "T", "Z", 1)
        self.g_7.adiciona_aresta("a8", "Z", "J", 1)

        self.lista_g_7 = ['J','a1','C','a2','E','a3','P','a4','M','a6','T','a7','Z','a8','J']

##############################################################################################
        self.g_1 = MeuGrafo()

        self.g_1.adiciona_vertice("A")
        self.g_1.adiciona_vertice("B")
        self.g_1.adiciona_vertice("C")
        self.g_1.adiciona_vertice("D")
        self.g_1.adiciona_vertice("E")

        self.g_1.adiciona_aresta("a1", "A", "B", 1)
        self.g_1.adiciona_aresta("a2", "B", "C", 1)
        self.g_1.adiciona_aresta("a3", "C", "A", 1)
        self.g_1.adiciona_aresta("a4", "C", "D", 1)
        self.g_1.adiciona_aresta("a5", "D", "E", 1)
        self.g_1.adiciona_aresta("a6", "E", "B", 1)

        self.lista_g_1 = ['B', 'a2', 'C', 'a4', 'D', 'a5', 'E', 'a6', 'B']
################################################################################################

        self.g_2 = MeuGrafo()

        self.g_2.adiciona_vertice("X")
        self.g_2.adiciona_vertice("Y")
        self.g_2.adiciona_vertice("Z")
        self.g_2.adiciona_vertice("W")

        self.g_2.adiciona_aresta("a1", "X", "Y", 3)
        self.g_2.adiciona_aresta("a2", "Y", "Z", 8)
        self.g_2.adiciona_aresta("a3", "Z", "W", 8)
        self.g_2.adiciona_aresta("a4", "W", "X", 5)
        self.g_2.adiciona_aresta("a5", "W", "Y", 2)

        self.lista_g_2 = ['Y', 'a2', 'Z', 'a3', 'W', 'a5', 'Y']
################################################################################################
        self.g_3 = MeuGrafo()

        self.g_3.adiciona_vertice("P")
        self.g_3.adiciona_vertice("Q")
        self.g_3.adiciona_vertice("R")
        self.g_3.adiciona_vertice("S")

        self.g_3.adiciona_aresta("a1", "P", "Q", 1)
        self.g_3.adiciona_aresta("a2", "Q", "R", 1)
        self.g_3.adiciona_aresta("a3", "R", "S", 1)
        self.g_3.adiciona_aresta("a4", "S", "P", 1)
        self.g_3.adiciona_aresta("a5", "R", "P", 1)

        self.lista_g_3 = ['P', 'a1', 'Q', 'a2', 'R', 'a5', 'P']
###############################################################################################
        self.g_4 = MeuGrafo()

        self.g_4.adiciona_vertice("M")
        self.g_4.adiciona_vertice("N")
        self.g_4.adiciona_vertice("O")
        self.g_4.adiciona_vertice("P")

        self.g_4.adiciona_aresta("a1", "M", "N", 1)
        self.g_4.adiciona_aresta("a2", "N", "O", 1)
        self.g_4.adiciona_aresta("a3", "O", "M", 1)
        self.g_4.adiciona_aresta("a4", "O", "P", 1)
        self.g_4.adiciona_aresta("a5", "P", "N", 1)

        self.lista_g_4 = ['N', 'a2', 'O', 'a4', 'P', 'a5', 'N']
##################################################################################################
        self.g_5 = MeuGrafo()

        self.g_5.adiciona_vertice("T")
        self.g_5.adiciona_vertice("U")
        self.g_5.adiciona_vertice("V")
        self.g_5.adiciona_vertice("W")
        self.g_5.adiciona_vertice("X")

        self.g_5.adiciona_aresta("a1", "T", "U", 1)
        self.g_5.adiciona_aresta("a2", "U", "V", 1)
        self.g_5.adiciona_aresta("a3", "V", "T", 1)
        self.g_5.adiciona_aresta("a4", "V", "W", 1)
        self.g_5.adiciona_aresta("a5", "W", "X", 1)
        self.g_5.adiciona_aresta("a6", "X", "T", 1)

        self.lista_g_5 = ['T', 'a1', 'U', 'a2', 'V', 'a4', 'W', 'a5', 'X', 'a6', 'T']
#####################################################################################################
        self.lista_g_6_cam = ['C', 'a3', 'M', 'a2', 'T']
        self.lista_g_1_cam = ['A', 'a1', 'B', 'a2', 'C']
        self.lista_g_2_cam = ['W', 'a3', 'Z', 'a2', 'Y']
        self.lista_g_3_cam = ['P', 'a1', 'Q', 'a2', 'R']
        self.lista_g_4_cam = ['M', 'a1', 'N', 'a2', 'O']
        self.lista_g_5_cam = ['T', 'a1', 'U', 'a2', 'V']
#####################################################################################################

        #Testes Alg de Djiskata
        self.g_3_ = MeuGrafo()

        self.g_3_.adiciona_vertice("P")
        self.g_3_.adiciona_vertice("Q")
        self.g_3_.adiciona_vertice("R")
        self.g_3_.adiciona_vertice("S")

        self.g_3_.adiciona_aresta("a1", "P", "Q", 5)
        self.g_3_.adiciona_aresta("a2", "Q", "R", 2)
        self.g_3_.adiciona_aresta("a3", "R", "S", 3)
        self.g_3_.adiciona_aresta("a4", "S", "P", 4)
        self.g_3_.adiciona_aresta("a5", "R", "P", 6)

        self.g_d5 = MeuGrafo()

        self.g_d5.adiciona_vertice('A')
        self.g_d5.adiciona_vertice('B')
        self.g_d5.adiciona_vertice('C')
        self.g_d5.adiciona_vertice('D')
        self.g_d5.adiciona_vertice('E')
        self.g_d5.adiciona_vertice('F')
        self.g_d5.adiciona_vertice('G')
        self.g_d5.adiciona_vertice('H')

        self.g_d5.adiciona_aresta('a1', 'A', 'B', 2)
        self.g_d5.adiciona_aresta('a2', 'A', 'C', 4)
        self.g_d5.adiciona_aresta('a3', 'B', 'E', 2)
        self.g_d5.adiciona_aresta('a4', 'B', 'D', 5)
        self.g_d5.adiciona_aresta('a5', 'D', 'F', 7)
        self.g_d5.adiciona_aresta('a6', 'D', 'G', 1)
        self.g_d5.adiciona_aresta('a7', 'D', 'H', 5)

        self.g_4 = MeuGrafo()

        self.g_4.adiciona_vertice("M")
        self.g_4.adiciona_vertice("N")
        self.g_4.adiciona_vertice("O")
        self.g_4.adiciona_vertice("P")

        self.g_4.adiciona_aresta("a1", "M", "N", 3)
        self.g_4.adiciona_aresta("a2", "N", "O", 2)
        self.g_4.adiciona_aresta("a3", "O", "M", 1)
        self.g_4.adiciona_aresta("a4", "O", "P", 6)
        self.g_4.adiciona_aresta("a5", "P", "N", 3)

        self.g_5 = MeuGrafo()

        self.g_5.adiciona_vertice("T")
        self.g_5.adiciona_vertice("U")
        self.g_5.adiciona_vertice("V")
        self.g_5.adiciona_vertice("W")
        self.g_5.adiciona_vertice("X")

        self.g_5.adiciona_aresta("a1", "T", "U", 1)
        self.g_5.adiciona_aresta("a2", "U", "V", 1)
        self.g_5.adiciona_aresta("a3", "V", "T", 1)
        self.g_5.adiciona_aresta("a4", "V", "W", 1)
        self.g_5.adiciona_aresta("a5", "W", "X", 1)
        self.g_5.adiciona_aresta("a6", "X", "T", 1)

        ##################################################################################################################
# Grafos com laco
        self.g_l1 = GrafoJSON.json_to_grafo('test_json/grafo_l1.json', MeuGrafo())

        self.g_l2 = GrafoJSON.json_to_grafo('test_json/grafo_l2.json', MeuGrafo())

        self.g_l3 = GrafoJSON.json_to_grafo('test_json/grafo_l3.json', MeuGrafo())

        self.g_l4 = GrafoBuilder().tipo(MeuGrafo()).vertices([v:=Vertice('D')]) \
            .arestas([Aresta('a1', v, v)]).build()

        self.g_l5 = GrafoBuilder().tipo(MeuGrafo()).vertices(3) \
            .arestas(3, lacos=1).build()

        # Grafos desconexos
        self.g_d = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), Vertice('C'), Vertice('D')]) \
            .arestas([Aresta('asd', a, b)]).build()

        self.g_d2 = GrafoBuilder().tipo(MeuGrafo()).vertices(4).build()

        # Grafo p\teste de remoção em casta
        self.g_r = GrafoBuilder().tipo(MeuGrafo()).vertices(2).arestas(1).build()

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = Aresta("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(TypeError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(TypeError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_remove_vertice(self):
        self.assertIsNone(self.g_r.remove_vertice('A'))
        self.assertFalse(self.g_r.existe_rotulo_vertice('A'))
        self.assertFalse(self.g_r.existe_rotulo_aresta('1'))
        with self.assertRaises(VerticeInvalidoError):
            self.g_r.get_vertice('A')
        self.assertFalse(self.g_r.get_aresta('1'))
        self.assertEqual(self.g_r.arestas_sobre_vertice('B'), set())

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def test_dfs(self):
        self.assertEqual(self.g_c.dfs('J'), self.g_c_dfs)
        self.assertEqual(self.g_c2.dfs('J'), self.g_c2_dfs)
        self.assertEqual(self.g_c3.dfs('J'), self.g_c3_dfs)
        self.assertEqual(self.g_c4.dfs('J'), self.g_c4_dfs)
        self.assertEqual(self.g_c5.dfs('A'), self.g_c5_dfs)
    def test_bfs(self):
        self.assertEqual(self.g_c.bfs('J'), self.g_c_bfs)
        self.assertEqual(self.g_c2.bfs('J'), self.g_c2_bfs)
        self.assertEqual(self.g_c3.bfs('J'), self.g_c3_bfs)
        self.assertEqual(self.g_c4.bfs('J'), self.g_c4_bfs)
        self.assertEqual(self.g_c5.bfs('A'), self.g_c5_bfs)
    def test_ha_ciclo(self):
        self.assertEqual(self.g_6.ha_ciclo(), self.lista_g_6)
        self.assertEqual(self.g_7.ha_ciclo(), self.lista_g_7)
        self.assertEqual(self.g_1.ha_ciclo(), self.lista_g_1)
        self.assertEqual(self.g_2.ha_ciclo(), self.lista_g_2)
        self.assertEqual(self.g_3.ha_ciclo(), self.lista_g_3)
        self.assertEqual(self.g_4.ha_ciclo(), self.lista_g_4)
        self.assertEqual(self.g_5.ha_ciclo(), self.lista_g_5)

    def test_caminho(self):
        self.assertEqual(self.g_6.caminho(3), self.lista_g_6_cam)
        self.assertEqual(self.g_1.caminho(3), self.lista_g_1_cam)
        self.assertEqual(self.g_2.caminho(3), self.lista_g_2_cam)
        self.assertEqual(self.g_3.caminho(3), self.lista_g_3_cam)
        self.assertEqual(self.g_4.caminho(3), self.lista_g_4_cam)
        self.assertEqual(self.g_5.caminho(3), self.lista_g_5_cam)
    def test_conexoes(self):
        self.assertTrue((self.g_c.conexo()))
        self.assertTrue((self.g_c2.conexo()))
        self.assertTrue((self.g_c3.conexo()))
        self.assertTrue((self.g_c4.conexo()))
        self.assertTrue((self.g_c5.conexo()))

    def test_dijkstra(self):
        self.assertEqual(self.g_6.dijkstra("J","M"),['J', 'T', 'M'] )
        self.assertEqual(self.g_1.dijkstra("A","D"), ['A', 'B', 'C', 'D'])
        self.assertEqual(self.g_2.dijkstra("X","Z"), ['X', 'Y', 'Z'])
        self.assertEqual(self.g_d5.dijkstra("A","H"), ['A', 'B', 'D', 'H'])
        self.assertEqual(self.g_4.dijkstra("M","P"), ['M', 'N', 'O', 'P'])
        self.assertEqual(self.g_5.dijkstra("T","X"), ['T', 'U', 'V', 'W', 'X'])
