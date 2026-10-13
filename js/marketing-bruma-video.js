/* One player and one frozen media selection per page visit. */
(() => {
  const section = document.getElementById('que-gestionamos');
  if (!section) return;
  const video = section.querySelector('video');
  const player = section.querySelector('.bv-player');
  const button = section.querySelector('.bv-play');
  const error = section.querySelector('.bv-error');
  if (!video || !player || !button || !error) return;

  const mobile = window.matchMedia('(max-width: 767px)').matches;
  const media = mobile ? {
    src: 'assets/marketing-video/bruma-cafetera-mobile-9x16-10s.mp4',
    poster: 'assets/marketing-video/bruma-poster-mobile.webp',
    width: 720, height: 1280
  } : {
    src: 'assets/marketing-video/bruma-cafetera-anuncio-10s-v2.mp4',
    poster: 'assets/marketing-video/bruma-poster-desktop.webp',
    width: 832, height: 1040
  };

  // Choose before the media load algorithm; preload stays "none".
  player.style.aspectRatio = `${media.width} / ${media.height}`;
  video.width = media.width;
  video.height = media.height;
  video.poster = media.poster;
  video.src = media.src;
  button.hidden = false;

  const reportError = () => { error.hidden = false; };
  video.addEventListener('error', reportError);
  video.addEventListener('playing', () => {
    error.hidden = true;
    // Move focus off the overlay before it is removed; keep native controls.
    if (document.activeElement === button) video.focus({preventScroll: true});
    button.hidden = true;
  });
  button.addEventListener('click', async () => {
    error.hidden = true;
    try { await video.play(); }
    catch (failure) {
      if (failure.name !== 'AbortError') reportError();
    }
  });
})();
