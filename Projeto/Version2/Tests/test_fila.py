import unittest
from unittest import TestCase
from Projeto.Version2.Core.Fila import Fila


class TestFila(TestCase):
    first = None

    def setUp(self):
        self.filaVazia = Fila()
        self.filaCheia = Fila()

        global first
        first = 3
        self.filaCheia.add_item(first)
        self.filaCheia.add_item(1)
        self.filaCheia.add_item(2)

    def test_is_empty(self):
        self.assertTrue(self.filaVazia.is_empty(), "TestIsEmpty| fila nao esta vazia")
        self.assertFalse(self.filaCheia.is_empty(), "TestIsEmpty| fila esta vazia")

    def test_get_size(self):
        self.assertEqual(self.filaVazia.get_size(), 0, "TestGetSize| fila vazia nao tem size 0")
        self.assertGreater(self.filaCheia.get_size(), 0, "TestGetSize| fila cheia nao tem size maior que 0")

    def test_peek(self):
        with self.assertRaises(IndexError, msg='TestPeek| Fila vazia nao esta vazia'):
            self.filaVazia.peek()

        self.assertEqual(self.filaCheia.peek(), 3, "TestPeek| Fila cheia esta vazia")

    def test_enqueue(self):
        self.filaVazia.enqueue(1)
        self.assertListEqual(self.filaVazia.data, [1], "TestEnqueue| Fila vazia nao fez enqueue")

        a = self.filaCheia.data
        a.append('a')
        self.filaCheia.enqueue('a')
        self.assertListEqual(self.filaCheia.data, a, "TestEnqueue| Fila vazia nao fez enqueue")

    # region Dequeue Test Methods
    def test_dequeue_equal_peek(self):
        global first
        self.assertEqual(self.filaCheia.peek(), self.filaCheia.dequeue(), "TestDequeue| 3| Dequeue diferente de peek")

    def test_dequeue_raises_IndexError(self):
        with self.assertRaises(IndexError, msg='|TestDequeueRaisesIndexError|'):
            self.filaVazia.dequeue()

    def test_dequeue_equal_first(self):
        global first
        self.assertEqual(self.filaCheia.dequeue(), first, "|TestDequeue=First|")

    def test_dequeue_equal_list_removed(self):
        lista = self.filaCheia.data[1:]
        self.filaCheia.dequeue()
        self.assertListEqual(self.filaCheia.data, lista, "|TestDequeue=First|")
        # endregion


def suite_fila_dequeue():
    suite = unittest.TestSuite()
    suite.addTest(TestFila("test_dequeue_equal_list_removed"))
    suite.addTest(TestFila("test_dequeue_equal_first"))
    suite.addTest(TestFila("test_dequeue_raises_IndexError"))
    suite.addTest(TestFila("test_dequeue_equal_peek"))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suiteDeq = suite_fila_dequeue()
    runner.run(suiteDeq)
