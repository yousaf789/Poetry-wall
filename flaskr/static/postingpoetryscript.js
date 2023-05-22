function getRandomPosition() {
  const x = Math.random() * ($('#poetry-wall').width() - 20);
  const y = Math.random() * ($('#poetry-wall').height() - 20);
  return { x, y };
}

function checkOverlap(newElement, otherElements) {
  const rect1 = newElement.getBoundingClientRect();

  for (let i = 0; i < otherElements.length; i++) {
    const rect2 = otherElements[i].getBoundingClientRect();

    if (
      rect1.left < rect2.right &&
      rect1.right > rect2.left &&
      rect1.top < rect2.bottom &&
      rect1.bottom > rect2.top
    ) {
      return true;
    }
  }

  return false;
}

$(document).ready(function () {
  $("#done-button").click(function (event) {
    event.preventDefault();

    const title = $("#title").val();
    const body = $("#body").val();

    if (title && body) {
      // Create a new poem element
      const poemElement = $('<div class="poem-point"></div>');

      // Add a title attribute to display the poem on hover
      poemElement.attr('title', `${title}\n\n${body}`);

      // Find a random position without overlap
      let position = getRandomPosition();
      let attempts = 0;
      const otherStars = $('.poem-point');

      while (checkOverlap(poemElement[0], otherStars) && attempts < 100) {
        position = getRandomPosition();
        attempts++;
      }

      // Position the new poem
      poemElement.css({
        top: position.y + 'px',
        left: position.x + 'px'
      });

      // Add the new poem to the poetry wall
      $("#poetry-wall").append(poemElement);

      // Reset the textarea
      $("#title").val("");
      $("#body").val("");
    }
  });
});

function displayPoem(title, body) {
  const poemElement = $('<div class="poem-point"></div>');
  poemElement.attr('title', `${title}\n\n${body}`);
  const position = getRandomPosition();
  poemElement.css({
    top: position.y + 'px',
    left: position.x + 'px'
  });
  $("#poetry-wall").append(poemElement);
}
