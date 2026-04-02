const form = document.getElementById('application-form');
const statusText = document.getElementById('form-status');
const addDetailsChoice = document.getElementById('addDetailsChoice');
const extraDetailsWrap = document.getElementById('extraDetailsWrap');
const extraDetails = document.getElementById('extraDetails');
const scrollProgress = document.getElementById('scroll-progress');

const onAddDetailsChange = () => {
  const shouldShow = addDetailsChoice.value === 'yes';
  extraDetailsWrap.classList.toggle('hidden', !shouldShow);
  extraDetails.required = shouldShow;
};

addDetailsChoice.addEventListener('change', onAddDetailsChange);
onAddDetailsChange();

window.addEventListener('scroll', () => {
  const pageHeight = document.documentElement.scrollHeight - window.innerHeight;
  const percent = pageHeight > 0 ? (window.scrollY / pageHeight) * 100 : 0;
  scrollProgress.style.width = `${percent}%`;
});

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.2 }
);

document.querySelectorAll('.reveal').forEach((element) => observer.observe(element));

form.addEventListener('submit', (event) => {
  event.preventDefault();

  if (!form.checkValidity()) {
    statusText.textContent = 'Please complete all required fields.';
    statusText.className = 'error';
    form.reportValidity();
    return;
  }

  const formData = new FormData(form);
  const applicantName = formData.get('fullName');

  statusText.textContent = `Thanks, ${applicantName}. Your application has been submitted.`;
  statusText.className = 'success';
  form.reset();
  onAddDetailsChange();
});
