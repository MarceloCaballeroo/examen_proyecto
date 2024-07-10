$(document).ready(function () {
  // URL de la API's
  const apiUrl = "http://localhost:3000/api/vehiculos";
  const urlRegiones = "http://localhost:3000/api/regiones";

  // Función para obtener los datos de la API
  function fetchVehiculos() {
    $.get(apiUrl, function (data) {
      if (data && data.length > 0) {
        renderVehiculos(data);
      } else {
        $("#vehiculos-container").html("<p>No hay vehículos disponibles.</p>");
      }
    }).fail(function () {
      $("#vehiculos-container").html("<p>Error al cargar los vehículos.</p>");
    });
  }

  function nombreVehiculos() {
      $.get(apiUrl, function (data) {
          if (data && data.length > 0) {
              let vehiculoSelect = $("#vehiculo");
              data.forEach((vehiculo) => {
                  vehiculoSelect.append(new Option(vehiculo.nombre, vehiculo.id));
              });
          } else {
              alert("No hay vehículos disponibles.");
          }
      }).fail(function () {
          alert("Error al cargar los vehículos.");
      });
  }

  function obtenerComunasPorRegion(regionNombre) {
      const urlComunas = `${urlRegiones}/${regionNombre}/comunas`;

      return fetch(urlComunas)
          .then(response => {
              if (!response.ok) {
                  throw new Error(`HTTP error! status: ${response.status}`);
              }
              return response.json();
          })
          .then(comunas => comunas)
  }

  function nombreRegiones() {
      $.get(urlRegiones, function (data) {
          if (data && data.length > 0) {
              let regionSelect = $("#region");
              data.forEach((region) => {
                  regionSelect.append(new Option(region.region, region.region));
              });

              regionSelect.on('change', function() {
                  const selectedRegionNombre = $(this).val();
                  const comunaSelect = $('#comuna');
                  comunaSelect.empty();
                  comunaSelect.append(new Option("Selecciona la comuna", "", true, true));

                  if (selectedRegionNombre) {
                      obtenerComunasPorRegion(selectedRegionNombre).then(comunas => {
                          if (comunas) {
                              comunas.forEach(comuna => {
                                  comunaSelect.append(new Option(comuna, comuna));
                              });
                          }
                      });
                  }
              });
          } else {
              alert("No hay regiones disponibles.");
          }
      }).fail(function (jqXHR, textStatus, errorThrown) {
          console.error(`Error al cargar las regiones: ${textStatus}, ${errorThrown}`);
          alert(`Error al cargar las regiones: ${textStatus}, ${errorThrown}`);
      });
  }

  // Función para renderizar los vehículos
  function renderVehiculos(vehiculos) {
      let html = "";
      vehiculos.forEach((vehiculo) => {
          html += `
              <div class="col-md-4">
                  <div class="card mb-4">
                      <img src="http://localhost:3000${vehiculo.imagen}" class="card-img-top" alt="${vehiculo.nombre}">
                      <div class="card-body">
                          <h5 class="card-title">${vehiculo.nombre}</h5>
                          <p class="card-text">${vehiculo.descripcion}</p>
                          <p class="card-text"><strong>Precio:</strong> $${vehiculo.precio}</p>
                      </div>
                  </div>
              </div>
          `;
      });
      $("#vehiculos-container").html(html);
  }

  // Llamar a la función para obtener y mostrar los vehículos
  fetchVehiculos();
  nombreVehiculos();
  nombreRegiones();

  // Manejar el envío del formulario de registro
  $('#register-form').on('submit', function(e) {
      e.preventDefault();
      const nombre = $('#nombre').val();
      const correo = $('#correo').val();
      const password = $('#password').val();
      const region = $('#region').val();
      const comuna = $('#comuna').val();
      const humano = $('#humano').is(':checked');
      if (humano) {
          // Aquí puedes agregar la lógica para registrar al usuario
          alert(`Registro: ${nombre}, Correo: ${correo}, Región: ${region}, Comuna: ${comuna}`);
      } else {
          alert('Por favor, confirma que eres humano.');
      }
  });

  const texto = "'Un pequeño paso para el hombre, un gran paso para la humanidad.'";
  const cita = "- Neil Armstrong";
  const elementoTexto = document.getElementById("animatedText");
  let indice = 0;
  let escribiendoCita = false; // Nuevo estado para controlar qué se está escribiendo

  function escribirTexto() {
      if (!escribiendoCita) {
          if (indice < texto.length) {
              elementoTexto.innerHTML += texto.charAt(indice);
              indice++;
              setTimeout(escribirTexto, 50); // Velocidad para el texto
          } else {
              // Una vez que el texto se ha completado, prepara para escribir la cita
              escribiendoCita = true;
              indice = 0; // Reinicia el índice para la cita
              elementoTexto.innerHTML += "<br>"; // Añade un salto de línea antes de la cita
              setTimeout(escribirTexto, 1000); // Espera un momento antes de empezar con la cita
          }
      } else {
          // Escribir la cita con una velocidad diferente
          if (indice < cita.length) {
              elementoTexto.innerHTML += cita.charAt(indice);
              indice++;
              setTimeout(escribirTexto, 100); // Velocidad para la cita
          }
      }
  }

  if (elementoTexto) {
      escribirTexto(); // Inicia la animación al cargar la página si el elemento existe
  }

  $("#socio-form").on("submit", function (e) {
      e.preventDefault();
      // Aquí puedes agregar la lógica para manejar el formulario
      alert("Formulario enviado");
  });
});
