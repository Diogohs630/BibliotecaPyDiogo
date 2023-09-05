from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)


    def _str_(self):
        return f'{self.nome}'
    

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=150)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)


    def _str_(self):
        return f'{self.nome}'
    

class Editora(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=150)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)


    def _str_(self):
        return f'{self.nome}'
    

class Categoria(models.Model):
    nome = models.CharField(max_length=50)


    def _str_(self):
        return self.nome


class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.FloatField(default=0.0)
    dataPublicacao = models.DateTimeField(auto_now=True)


    def _str_(self):
        return f'{self.nome}'
    

class Leitores(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14)


    def _str_(self):
        return f'{self.nome}'
    

class Emprestimo(models.Model):
    dataEmprestimo = models.DateField(auto_now=False)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    leitor = models.ForeignKey(Leitores, on_delete=models.CASCADE)
    dataDevolucao = models.DateField(auto_now=False)


    def _str_(self):
        return f'{self.dataEmprestimo} {self.livro} {self.leitor} {self.dataDevolucao}'


