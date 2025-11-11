INSERT INTO system_param (`key`, value_num)
VALUES ('SPACE_BETWEEN_STREETS_M', 1);

INSERT INTO format_type (code, description) VALUES
('retangulo', 'Área retangular'),
('triangulo', 'Área triangular');

INSERT INTO product (name, dosage_per_m2) VALUES
('Fosfato Monoamônico', 5),
('Diclorofenoxiacético', 0.15);

INSERT INTO culture (name, product_id, format_id, street_size_m)
SELECT 'milho', p.id, f.id, 1
  FROM product p, format_type f
 WHERE p.name='Fosfato Monoamônico' AND f.code='retangulo';

INSERT INTO culture (name, product_id, format_id, street_size_m)
SELECT 'laranja', p.id, f.id, 2
  FROM product p, format_type f
 WHERE p.name='Diclorofenoxiacético' AND f.code='triangulo';
