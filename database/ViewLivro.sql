select
	lv.id as id_livro,
	lv.nome as nome_livro,
	aut.nome as autor,
	ed.nome as editora,
	lv.preco
from
	app_livro lv
	Join app_categoria cat on cat.id = lv.categoria_id
	Join app_editora ed on ed.id = lv.editora_id
	Join app_autor aut on aut.id = lv.autor_id