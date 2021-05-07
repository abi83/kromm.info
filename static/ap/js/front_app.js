const App = {
      data() {
        return {
          loading: false,
          pageData: {
            title: 'Аква пром',
            short: 'данные загружаются...',
            text: 'данные загружаются...',}
        };
      },
      async mounted() {
        this.loading = true;
        this.pageData = await request('http://localhost:3000/products/index/');
        this.loading = false;
      }
};
// Vue.component('loader', {
//   template:`
//     <div class="loader" v-if="loading">
//       <span>Данные загружаются</span>
//     </div>
//   `
// })
// Vue.createApp(App).mount('#vue-app');


async function request(url, method='GET', data=null) {
  try {
    const headers = {}
    let body
    if (data) {
      headers['Content-Type'] = 'application/json'
      body = JSON.stringify(data)
    }
    const response = await fetch(url, {method, headers, body})
    return response.json()
  } catch (error) {
    console.log('Error:', error.message)
  }
}

function showNextProject() {
        //show 'next-project' item
        let images = Array.from(document.querySelectorAll('.prj-image'));
        let texts = Array.from(document.querySelectorAll('.prj-text'));
        let active = images.find((element) => {
          return !element.classList.contains('prj-hidden');
        })
        active.classList.add('prj-hidden');
        let activeIndex = images.indexOf(active)
        texts[activeIndex].classList.add('prj-hidden')
        if (activeIndex + 1 < images.length){
          images[activeIndex+1].classList.remove('prj-hidden');
          texts[activeIndex+1].classList.remove('prj-hidden');
        } else {
          images[0].classList.remove('prj-hidden');
          texts[0].classList.remove('prj-hidden');
        }
}

document.querySelector('#next-project-button')
        .addEventListener('click', showNextProject);


///animate on scroll
let productGridObserver = new IntersectionObserver(function(entries) {
  if(entries[0].isIntersecting === true) {
    for (let entry of entries){
      entry.target.classList.add('product-grid-item-scroll');
    }
  } else {
    for (let entry of entries){
      entry.target.classList.remove('product-grid-item-scroll');
    }
  }
}, { threshold: [0.5] });

for (let el of document.querySelectorAll('.product-grid-item')){
  productGridObserver.observe(el);
}

let secondScreenObserver = new IntersectionObserver(function(entries) {
  if (entries[0].isIntersecting === true) {
    document.querySelector('main').style.marginTop = '0';
    document.querySelector('.navbar').classList.remove('navbar-modified');
    console.log('first screen')
  } else {
    console.log('not first screen')
    document.querySelector('main').style.marginTop = '10xh';
    document.querySelector('.navbar').classList.add('navbar-modified');
    
  }
}, {threshold: [0.75]})

secondScreenObserver.observe(document.querySelector('#first-screen'))


//accordion animation
let acc = document.getElementsByClassName("accordion");

for (let i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("accordion-active");
        let panel = this.nextElementSibling;
        panel.classList.toggle("panel-active");
    });
}

//main slider auto animation
function returnCheckedIndex(elements) {
  let checkedIndex = 0;
  for (let element of elements) {
    if (element.checked) {
      return checkedIndex
    } else {
      checkedIndex++
    }
  }
}
function mainSliderAnimate() {
  let sliderTriggers = document.querySelectorAll('input.slider-radio');
  const checkedIndex = returnCheckedIndex(sliderTriggers);
  if (checkedIndex <2){
    sliderTriggers.item(checkedIndex).checked = false;
    sliderTriggers.item(checkedIndex+1).checked = true;
  } else {
    sliderTriggers.item(checkedIndex).checked = false;
    sliderTriggers.item(0).checked = true;
  }
}

setInterval(()=> {
  mainSliderAnimate();
  showNextProject();
}, 3500)
