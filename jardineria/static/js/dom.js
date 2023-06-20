const image = document.querySelector('.zoom');

image.addEventListener('mouseover', () => {
  image.classList.add('zoom:hover');
});

image.addEventListener('mouseout', () => {
  image.classList.remove('zoom:hover');
});

Text.addEventListener('mouseover', () => {
  Text.classList.add('zoom:hover');
});

Text.addEventListener('mouseout', () => {
  Text.classList.remove('zoom:hover');
});