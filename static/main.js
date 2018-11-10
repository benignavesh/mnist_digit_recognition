document.addEventListener('DOMContentLoaded', function () {
  const imageForm = document.querySelector('#imageForm')
  const selectImage = document.querySelector('#iamgeinput')
  const predict = document.querySelector('#submit')
  const clear = document.querySelector('#clear')
  // const uploadedImage = document.querySelector('#uploadedfile')

  // initializing the drawing board

  const customBoard = new DrawingBoard.Board('drawingBorad', {
    background: '#000000',
    color: '#ffffff',
    controlsPosition: 'center',
    size: 24,
    controls: [{
        Navigation: {
          back: false,
          forward: false
        }
      },
      'DrawingMode'
    ],
    webStorage: false,
    stretchImg: true,
    enlargeYourContainer: true
  })

  const makeImage = url => {
    return new Promise(res => {
      // uploadedImage.src = url
      res(url)
    })
  }

  clear.addEventListener('click', function (e) {
    imageForm.reset()
    selectImage.value = ''
    // uploadedImage.src = ''
    console.log(customBoard);
    customBoard.reset({ background: true })
  })

  predict.addEventListener('click', function (e) {
    makeImage(customBoard.getImg()).then(url => {
      onPredictClick(url)
    })
  })

  imageForm.addEventListener('submit', function (e) {
    e.preventDefault()
  })

  selectImage.addEventListener('change', function (e) {
    const file = e.target.files[0] ? e.target.files[0] : null
    // if (file) {
    //   uploadedImage.src = window.URL.createObjectURL(file)
    // }
  })
})