function openLinkOnImageClick() {
    sitesArr = [];
    document.querySelectorAll(".card-text a").forEach((site) => sitesArr.push(site));

    for(let i = 0; i < sitesArr.length; i++) {
        document.querySelectorAll(".card-img-top")[i].addEventListener("click", () => window.open(sitesArr[i]));
    }
}

function goToHomeOnLogoClick() {
    document.querySelector(".logoimg").addEventListener("click", () => window.location.href = "https://easyvax.herokuapp.com/")
}

openLinkOnImageClick();
goToHomeOnLogoClick();