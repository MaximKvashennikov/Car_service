function ready() {
  function scrollTo(element) {
    window.scroll({
      left: 0,
      top: element.offsetTop,
      behavior: "smooth",
      block: "center",
    });
  }

  document.querySelector("#button_services").addEventListener("click", () => {
    scrollTo(document.querySelector("#repair_services"));
  });
  document.querySelector("#button_address").addEventListener("click", () => {
    scrollTo(document.querySelector("#repair_address"));
  });
  document.querySelector("#button_owner").addEventListener("click", () => {
    scrollTo(document.querySelector("#repair_owner"));
  });
  document.querySelector("#button_feedback").addEventListener("click", () => {
    scrollTo(document.querySelector("#repair_feedback"));
  });
}

document.addEventListener("DOMContentLoaded", ready);

function Menu(e) {
  let list = document.querySelector("ul");
  e.name === "menu"
    ? ((e.name = "close"),
      list.classList.add("top-[80px]"),
      list.classList.add("opacity-100"),
      list.classList.remove("md:static", "absolute"))
    : ((e.name = "menu"),
      list.classList.remove("top-[80px]"),
      list.classList.remove("opacity-100"),
      list.classList.add("md:static", "absolute"));
}
