const filterMenu = document.querySelector('.filter-menu')

function openBurgerMenu() {
  filterMenu.classList.remove('menu-closed')
  filterMenu.classList.add('menu-open')
}

function closedBurgerMenu() {
  filterMenu.classList.remove('menu-open')
  filterMenu.classList.add('menu-closed')
}
