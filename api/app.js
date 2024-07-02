const express = require('express');
const path = require('path');
const cors = require('cors');
const vehiculosRouter = require('./routes/vehiculos');
const regionesRouter = require('./routes/regiones'); // Añadir esto

const app = express();
const port = 3000;

app.use(cors());
app.use('/api/vehiculos', vehiculosRouter);
app.use('/api/regiones', regionesRouter); // Añadir esto
app.use('/images', express.static(path.join(__dirname, 'public/images')));

app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});