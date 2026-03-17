# Crud_alberto
Atividade

# 🐞 CRUD de Produtos em Python (Com Bugs Intencionais)

## 📌 Descrição
Este projeto consiste em um CRUD (Create, Read, Update, Delete) simples em Python para cadastro de produtos.

O objetivo é demonstrar falhas comuns em sistemas, sendo utilizado para práticas de **testes de software** e identificação de bugs.

---

## ⚙️ Funcionalidades

- Criar produto (ID, nome e preço)
- Listar produtos cadastrados
- Atualizar produto
- Deletar produto

---

## 🐞 Bugs Intencionais

### 🔴 Bug 1: Permite preço negativo
- **Local:** `create_product`
- **Descrição:** O sistema permite cadastrar produtos com preço negativo.
- **Impacto:** Dados inválidos podem ser armazenados.
- **Exemplo:** Produto com preço `-100`.

---

### 🔴 Bug 2: Contagem incorreta de produtos
- **Local:** `read_products`
- **Descrição:** O total de produtos é exibido com `+1`, gerando valor incorreto.
- **Impacto:** Informação errada para o usuário.
- **Exemplo:** 2 produtos cadastrados → mostra 3.

---

### 🔴 Bug 3: Atualiza todos os produtos
- **Local:** `update_product`
- **Descrição:** A função ignora o ID e atualiza todos os produtos.
- **Impacto:** Todos os dados podem ser alterados indevidamente.
- **Exemplo:** Atualizar um produto altera todos.

---

### 🔴 Bug 4: Remove produto incorreto
- **Local:** `delete_product`
- **Descrição:** Remove sempre o primeiro produto da lista.
- **Impacto:** Pode deletar o produto errado.
- **Exemplo:** Tentar deletar ID 2 remove o ID 1.
```bash
