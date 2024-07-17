$(document).ready(function () {
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
});
