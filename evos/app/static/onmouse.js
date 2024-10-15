
const dishes = document.querySelectorAll('.dish')

dishes.forEach(dish => {
    const add_window = dish.querySelector('.add_window')
    const dish_info = dish.querySelector('.dish_info')

    dish.addEventListener('mouseover', () => {
        add_window.style.display = 'flex'
    })
    dish.addEventListener('mouseout', () => {
        add_window.style.display = 'none'
    })
})