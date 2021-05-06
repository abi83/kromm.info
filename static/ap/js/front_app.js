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
let observer = new IntersectionObserver(function(entries) {
  if(entries[0].isIntersecting === true) {
    for (let entry of entries){
      entry.target.classList.add('product-grid-item-scroll');
      // console.log(entry.target)
    }
  } else {
    for (let entry of entries){
      entry.target.classList.remove('product-grid-item-scroll');
      // console.log(entry.target)
    }
  }
}, { threshold: [0.5] });

for (let el of document.querySelectorAll('.product-grid-item')){
  observer.observe(el);
}


//accordion animation
let acc = document.getElementsByClassName("accordion");

for (let i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("accordion-active");
        let panel = this.nextElementSibling;
        panel.classList.toggle("panel-active");
        // if (panel.style.display === "block") {
        //     panel.style.display = "none";
        // } else {
        //     panel.style.display = "block";
        // }
    });
}

//main slider auto animation
// document.querySelectorAll('input.slider-radio')[0].checked = true

