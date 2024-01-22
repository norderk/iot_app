/* This update page layout? */
// eslint-disable-next-line no-unused-vars
function getPage (pageName) {
  if (pageName === '' | pageName === 'home') {
    document.location.href = '/'
  } else {
    location.replace(pageName)
  }
}
