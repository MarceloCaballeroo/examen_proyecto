const express = require('express');
const router = express.Router();
const fs = require('fs');
const path = require('path');

// Ruta al archivo JSON de las regiones y comunas
const regionesFilePath = path.join(__dirname, '../data/chileRegions.json');

// Leer el archivo JSON y parsearlo
function getRegionesData() {
  const data = fs.readFileSync(regionesFilePath);
  return JSON.parse(data);
}

router.get('/', (req, res) => {
  const regionesData = getRegionesData();
  res.json(regionesData.regiones);
});

router.get('/:region/comunas', (req, res) => {
  const regionesData = getRegionesData();
  const region = regionesData.regiones.find(r => r.region === req.params.region);
  
  if (region) {
    res.json(region.comunas);
  } else {
    res.status(404).send('Región no encontrada');
  }
});

module.exports = router;
