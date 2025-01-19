
// زر القائمة الجانبية
const menuBtn = document.getElementById('menu-btn');
const menu = document.getElementById('menu');

menuBtn.addEventListener('click', () => {
  menu.classList.toggle('active'); // إضافة أو إزالة الكلاس "active"
});

document.addEventListener("DOMContentLoaded", function() {
  var menuBtn = document.getElementById("menu-btn");
  var menu = document.getElementById("menu");

  menuBtn.addEventListener("click", function() {
    if (menu.style.display === "none" || menu.style.display === "") {
      menu.style.display = "block";
    } else {
      menu.style.display = "none";
    }
  });
});


/////hhdhhhhdhhhhhdhhhhd


      document.addEventListener("DOMContentLoaded", function() {
  function showMore(event) {
       var toggleLink = event.target;
      var paragraphId = toggleLink.getAttribute("data-paragraph-id");
      var paragraph = document.getElementById(paragraphId);
        
      if (paragraph.classList.contains("collapsed")) {
          paragraph.classList.remove("collapsed");
          toggleLink.textContent = "إخفاء";
      } else {
          paragraph.classList.add("collapsed");
          toggleLink.textContent = "عرض المزيد";
      }
  }

  var toggleLinks = document.querySelectorAll(".toggle-link");
  toggleLinks.forEach(function(link) {
      var paragraphId = link.id.replace("toggle-link", "paragraph");
      link.setAttribute("data-paragraph-id", paragraphId);
      link.addEventListener("click", showMore);
  });

  // Initialize the paragraphs to show only half
  var paragraphs = document.querySelectorAll(".paragraph");
  paragraphs.forEach(function(paragraph) {
      paragraph.classList.add("collapsed");
  });
});
//navbar

let lastScrollTop = 0;
    const navbar = document.querySelector('.navbar');
  
    window.addEventListener('scroll', function() {
      if (window.innerWidth <= 768) { // Apply only on small screens
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        if (scrollTop > lastScrollTop) {
          // Scroll down
          navbar.style.top = '-100px'; // Adjust this value based on your navbar height
        } else {
          // Scroll up
          navbar.style.top = '0';
        }
        lastScrollTop = scrollTop;
      }
    });