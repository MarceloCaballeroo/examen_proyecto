const express = require('express');
const router = express.Router();

const vehiculos = [
    {
      id: 1,
      nombre: 'Toyota Corolla',
      descripcion: 'Un vehículo compacto confiable y eficiente.',
      precio: 20000,
      imagen: '/images/toyota.jpg'
    },
    {
      id: 2,
      nombre: 'Honda Civic',
      descripcion: 'Un sedán deportivo con un diseño moderno.',
      precio: 22000,
      imagen: '/images/honda.jpg'
    },
    {
      id: 3,
      nombre: 'Ford Mustang',
      descripcion: 'Un icónico automóvil deportivo con un potente motor.',
      precio: 35000,
      imagen: '/images/ford.jpg'
    }
  ];

router.get('/', (req, res) => {
  res.json(vehiculos);
});

router.get('/:id', (req, res) => {
  const vehiculo = vehiculos.find(v => v.id == req.params.id);
  if (vehiculo) {
    res.json(vehiculo);
  } else {
    res.status(404).send('Vehículo no encontrado');
  }
});

module.exports = router;
