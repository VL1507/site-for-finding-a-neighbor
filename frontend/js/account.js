const userNameArea = document.querySelector('.user-name')
const userInterestsArea = document.querySelector('.user-interests')
const userAboutArea = document.querySelector('.user-about')

const userNameAreaAnket = document.querySelector('.user-anket-name')
const userInterestsAreaAnket = document.querySelector('.user-anket-interests')
const userAboutAreaAnket = document.querySelector('.user-anket-about')
const userTicketAreaAnket= document.querySelector('.user-anket-ticket')

let userName = 'Дмитрий'
let userInterests = 'Спорт, живопись'
let userAbout = 'Спортивный, разносторонний, приятный в общении, дружелюбный человек'
let userTicket = '123 456 789'

userNameArea.innerHTML = 'Имя: ' + userName
userInterestsArea.innerHTML = userInterests
userAboutArea.innerHTML = userAbout

userNameAreaAnket.innerHTML = 'Имя: ' + userName
userInterestsAreaAnket.innerHTML = userInterests
userAboutAreaAnket.innerHTML = userAbout
userTicketAreaAnket.innerHTML = 'ticket: ' + userTicket


function createAnket() {
  swal("Анкета успешно создана!", "Ваша анкета была создана, посмотреть ее можно в личном кабинете или в общем списке (помечена красным)", "success");
}