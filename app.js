const translations = {
  ka: {
    pageTitle: 'ბედი ქართლისა — საქართველოს საინფორმაციო პორტალი',
    skipToContent: 'შინაარსზე გადასვლა',
    brandHome: 'ბედი ქართლისა — მთავარი გვერდი',
    brandName: 'ბედი ქართლისა',
    mainNavigation: 'მთავარი მენიუ',
    overview: 'მიმოხილვა',
    sources: 'წყაროები',
    seeMore: 'მეტის ნახვა',
    seeLess: 'ნაკლების ნახვა',
    publicPortal: 'საჯარო პორტალი',
    publicInfoNote: 'ინფორმაცია საჯარო წყაროებიდან.',
    publicInformation: 'საჯარო ინფორმაცია',
    languageSelector: 'ენის არჩევა',
    portalEyebrow: 'საქართველო · მოვლენები და კონტექსტი',
    headlineFirst: 'საქართველო,',
    headlineSecond: 'ფაქტები კონტექსტში.',
    headingCopy: 'საქართველოს საზოგადოებრივი ცხოვრების მნიშვნელოვანი თემები და საჯარო წყაროები ერთ სივრცეში.',
    asideCaption: 'საჯარო წყაროები · გასაგები კონტექსტი',
    overviewEyebrow: 'თემები',
    overviewTitle: 'საქართველოს მიმოხილვა',
    areaCount: '18 მიმართულება',
    exploreTopic: 'თემის ნახვა',
    primarySourcesEyebrow: 'პირველწყაროები',
    primarySourcesTitle: 'დაიწყეთ საჯარო წყაროებით',
    allSources: 'ყველა წყარო',
    aboutPortal: 'პორტალის შესახებ',
    publicNotPersonal: 'საჯარო ინფორმაცია ყველასთვის.',
    aboutPortalCopy: 'პორტალი აერთიანებს საზოგადოებისთვის მნიშვნელოვან თემებს და მკითხველს საჯარო წყაროებთან აკავშირებს.',
    editorialDisclaimer: 'საინფორმაციო მიმოხილვა · არა ოფიციალური განცხადება',
    whatToFollow: 'რას მოიცავს ეს მიმართულება',
    relatedSources: 'დაკავშირებული წყაროები',
    checkSources: 'დეტალებისა და განახლებული მონაცემებისთვის იხილეთ წყაროები.',
    sourcePending: 'ამ თემისთვის წყაროები ჯერ მზადდება.',
    sourceEyebrow: 'გადაამოწმეთ პირველწყაროში',
    sourcesTitle: 'საჯარო წყაროები',
    officialSources: 'ოფიციალური წყაროები',
    sourcesIntro: 'მონაცემების გამოყენებამდე გადაამოწმეთ გამოქვეყნების თარიღი, განმარტებები და მეთოდოლოგია.',
    footerBrand: 'ბედი ქართლისა · საჯარო საინფორმაციო პორტალი',
    footerMotto: 'ინფორმაცია — წყაროებით. კონტექსტი — პასუხისმგებლობით.'
  },
  en: {
    pageTitle: 'Fate of Georgia — Public Information Portal',
    skipToContent: 'Skip to content',
    brandHome: 'Fate of Georgia home',
    brandName: 'Fate of Georgia',
    mainNavigation: 'Main navigation',
    overview: 'Overview',
    sources: 'Sources',
    seeMore: 'See more',
    seeLess: 'See less',
    publicPortal: 'Public portal',
    publicInfoNote: 'Information from public sources.',
    publicInformation: 'PUBLIC INFORMATION',
    languageSelector: 'Select language',
    portalEyebrow: 'GEORGIA · EVENTS AND CONTEXT',
    headlineFirst: 'Georgia,',
    headlineSecond: 'facts in context.',
    headingCopy: 'Key areas of public life in Georgia and public sources, brought together.',
    asideCaption: 'Public sources · Clear context',
    overviewEyebrow: 'AREAS OF FOCUS',
    overviewTitle: 'Georgia overview',
    areaCount: '18 AREAS',
    exploreTopic: 'Explore topic',
    primarySourcesEyebrow: 'PRIMARY SOURCES',
    primarySourcesTitle: 'Start with public sources',
    allSources: 'All sources',
    aboutPortal: 'ABOUT THIS PORTAL',
    publicNotPersonal: 'Public information for everyone.',
    aboutPortalCopy: 'This portal brings together topics of public interest and connects readers to public sources.',
    editorialDisclaimer: 'INFORMATIONAL OVERVIEW · NOT AN OFFICIAL STATEMENT',
    whatToFollow: 'WHAT THIS AREA COVERS',
    relatedSources: 'RELATED SOURCES',
    checkSources: 'Consult the sources for details and up-to-date information.',
    sourcePending: 'Sources for this topic are being prepared.',
    sourceEyebrow: 'CHECK THE ORIGINAL',
    sourcesTitle: 'Public sources',
    officialSources: 'OFFICIAL SOURCES',
    sourcesIntro: 'Before using data, check its publication date, definitions, and methodology.',
    footerBrand: 'FATE OF GEORGIA · PUBLIC INFORMATION PORTAL',
    footerMotto: 'Information with sources. Context with care.'
  }
};

const sources = {
  geostat: {
    url: 'https://www.geostat.ge/',
    name: { ka: 'საქართველოს სტატისტიკის ეროვნული სამსახური', en: 'National Statistics Office of Georgia' },
    description: { ka: 'ოფიციალური სტატისტიკა საქართველოს შესახებ.', en: 'Official statistics about Georgia.' }
  },
  parliament: {
    url: 'https://www.parliament.ge/',
    name: { ka: 'საქართველოს პარლამენტი', en: 'Parliament of Georgia' },
    description: { ka: 'პარლამენტის საქმიანობა, კანონპროექტები და სხდომები.', en: 'Parliamentary activity, draft laws, and sessions.' }
  },
  matsne: {
    url: 'https://matsne.gov.ge/',
    name: { ka: 'საქართველოს საკანონმდებლო მაცნე', en: 'Legislative Herald of Georgia' },
    description: { ka: 'საქართველოს საკანონმდებლო და სხვა სამართლებრივი აქტები.', en: 'Legislation and other legal acts of Georgia.' }
  },
  nbg: {
    url: 'https://nbg.gov.ge/',
    name: { ka: 'საქართველოს ეროვნული ბანკი', en: 'National Bank of Georgia' },
    description: { ka: 'მონეტარული პოლიტიკა და მაკროეკონომიკური მონაცემები.', en: 'Monetary policy and macroeconomic data.' }
  },
  mfa: {
    url: 'https://mfa.gov.ge/',
    name: { ka: 'საქართველოს საგარეო საქმეთა სამინისტრო', en: 'Ministry of Foreign Affairs of Georgia' },
    description: { ka: 'ოფიციალური განცხადებები და საგარეო ურთიერთობების შესახებ ინფორმაცია.', en: 'Official statements and information on foreign relations.' }
  }
};

const topics = [
  { id: 'science', title: ['მეცნიერება', 'Science'], detail: ['კვლევა, ინოვაცია და სამეცნიერო ინსტიტუტები.', 'Research, innovation, and scientific institutions.'], sources: [] },
  { id: 'environment', title: ['ეკოლოგია', 'Environment'], detail: ['გარემოს დაცვა, ბუნებრივი რესურსები და კლიმატი.', 'Environmental protection, natural resources, and climate.'], sources: ['geostat'] },
  { id: 'enterprise', title: ['მეწარმეობა', 'Enterprise'], detail: ['ბიზნესი, ინვესტიციები და ეკონომიკა.', 'Business, investment, and the economy.'], sources: ['geostat', 'nbg'] },
  { id: 'agriculture', title: ['მეურნეობა', 'Agriculture'], detail: ['სოფლის მეურნეობა და სურსათის წარმოება.', 'Agriculture and food production.'], sources: ['geostat'] },
  { id: 'defence', title: ['თავდაცვა', 'Defence'], detail: ['ქვეყნის თავდაცვა და უსაფრთხოების პოლიტიკა.', 'National defence and security policy.'], sources: ['parliament', 'matsne'] },
  { id: 'infrastructure', title: ['ინფრასტრუქტურა', 'Infrastructure'], detail: ['გზები, წყალი, ენერგია და სხვა ძირითადი სისტემები.', 'Roads, water, energy, and other essential systems.'], sources: ['geostat'] },
  { id: 'justice', title: ['სასამართლო', 'Courts'], detail: ['მართლმსაჯულება და სასამართლოების საქმიანობა.', 'Justice and the work of the courts.'], sources: ['matsne'] },
  { id: 'governance', title: ['საჯარო მმართველობა', 'Public governance'], detail: ['სახელმწიფო ინსტიტუტები, საჯარო სერვისები და ანგარიშვალდებულება.', 'Public institutions, public services, and accountability.'], sources: ['parliament', 'matsne'] },
  { id: 'education', title: ['განათლება', 'Education'], detail: ['სკოლები, უმაღლესი და პროფესიული განათლება.', 'Schools, higher education, and vocational education.'], sources: ['geostat'] },
  { id: 'health', title: ['ჯანმრთელობა', 'Health'], detail: ['ჯანდაცვის ხელმისაწვდომობა და საზოგადოებრივი ჯანმრთელობა.', 'Access to healthcare and public health.'], sources: ['geostat'] },
  { id: 'employment', title: ['შრომა და დასაქმება', 'Work and employment'], detail: ['სამუშაო პირობები, ხელფასები და შრომითი უფლებები.', 'Working conditions, wages, and labour rights.'], sources: ['geostat', 'matsne'] },
  { id: 'cost-of-living', title: ['ცხოვრების ღირებულება', 'Cost of living'], detail: ['ფასები, ინფლაცია და საოჯახო ხარჯები.', 'Prices, inflation, and household spending.'], sources: ['geostat', 'nbg'] },
  { id: 'social-protection', title: ['სოციალური დაცვა', 'Social protection'], detail: ['პენსიები, დახმარებები და სოციალური სერვისები.', 'Pensions, benefits, and social services.'], sources: ['matsne'] },
  { id: 'housing', title: ['საცხოვრებელი', 'Housing'], detail: ['საცხოვრებლის ხელმისაწვდომობა და საბინაო პირობები.', 'Housing affordability and living conditions.'], sources: ['geostat'] },
  { id: 'transport', title: ['ტრანსპორტი', 'Transport'], detail: ['საზოგადოებრივი ტრანსპორტი და გადაადგილება.', 'Public transport and mobility.'], sources: ['geostat'] },
  { id: 'rights-safety', title: ['უფლებები და უსაფრთხოება', 'Rights and safety'], detail: ['ადამიანის უფლებები, საზოგადოებრივი უსაფრთხოება და პოლიციის საქმიანობა.', 'Human rights, public safety, and policing.'], sources: ['matsne'] },
  { id: 'culture-sport', title: ['კულტურა და სპორტი', 'Culture and sport'], detail: ['კულტურული ცხოვრება, მემკვიდრეობა და სპორტი.', 'Cultural life, heritage, and sport.'], sources: ['geostat'] },
  { id: 'foreign-relations', title: ['საგარეო ურთიერთობები', 'Foreign relations'], detail: ['საერთაშორისო ურთიერთობები და საქართველოს ადგილი მსოფლიოში.', 'International relations and Georgia’s place in the world.'], sources: ['mfa'] }
];

let language = 'ka';
let categoriesExpanded = false;
const visibleCategoryCount = 5;

function text(key) {
  return translations[language][key];
}

function localized(values) {
  return values[language === 'ka' ? 0 : 1];
}

function element(tag, className, content) {
  const result = document.createElement(tag);
  if (className) result.className = className;
  if (content !== undefined) result.textContent = content;
  return result;
}

function sourceCard(source) {
  const link = element('a', 'source-card');
  link.href = source.url;
  link.target = '_blank';
  link.rel = 'noopener noreferrer';
  const icon = element('span', 'source-icon', '↗');
  icon.setAttribute('aria-hidden', 'true');
  const details = element('span', 'source-details');
  details.append(element('strong', '', source.name[language]), element('span', '', source.description[language]));
  const external = element('span', 'source-external', '↗');
  external.setAttribute('aria-hidden', 'true');
  link.append(icon, details, external);
  return link;
}

function currentPage() {
  const id = location.hash.slice(1);
  return id === 'sources' || topics.some((topic) => topic.id === id) ? id : 'overview';
}

function render() {
  const page = currentPage();
  const selectedTopic = topics.find((topic) => topic.id === page);
  document.documentElement.lang = language;
  document.title = text('pageTitle');
  document.querySelectorAll('[data-i18n]').forEach((item) => {
    item.textContent = text(item.dataset.i18n);
  });
  document.querySelectorAll('[data-i18n-aria-label]').forEach((item) => {
    item.setAttribute('aria-label', text(item.dataset.i18nAriaLabel));
  });
  document.querySelectorAll('[data-language]').forEach((button) => {
    const active = button.dataset.language === language;
    button.classList.toggle('is-active', active);
    button.setAttribute('aria-pressed', String(active));
  });

  const overviewLink = document.querySelector('#overview-link');
  overviewLink.classList.toggle('is-active', page === 'overview');
  if (page === 'overview') overviewLink.setAttribute('aria-current', 'page');
  else overviewLink.removeAttribute('aria-current');

  const categoryList = document.querySelector('#category-list');
  const scrollTop = categoryList.scrollTop;
  categoryList.replaceChildren();
  categoryList.classList.toggle('is-expanded', categoriesExpanded);
  const navigation = [
    ...topics.map((topic) => ({ id: topic.id, name: localized(topic.title) })),
    { id: 'sources', name: text('sources') }
  ].sort((a, b) => a.name.localeCompare(b.name, language));
  navigation.forEach((item, index) => {
    const link = element('a', 'nav-link', item.name);
    link.href = `#${item.id}`;
    link.hidden = !categoriesExpanded && index >= visibleCategoryCount;
    if (item.id === page) {
      link.classList.add('is-active');
      link.setAttribute('aria-current', 'page');
    }
    categoryList.append(link);
  });
  categoryList.scrollTop = categoriesExpanded ? scrollTop : 0;
  const navToggle = document.querySelector('#nav-toggle');
  navToggle.textContent = text(categoriesExpanded ? 'seeLess' : 'seeMore');
  navToggle.setAttribute('aria-expanded', String(categoriesExpanded));

  const grid = document.querySelector('#topic-grid');
  grid.replaceChildren();
  topics.forEach((topic, index) => {
    const card = element('a', 'topic-card');
    card.href = `#${topic.id}`;
    const action = element('span', 'topic-link');
    const arrow = element('span', '', '→');
    arrow.setAttribute('aria-hidden', 'true');
    action.append(element('span', '', text('exploreTopic')), arrow);
    card.append(element('span', 'topic-number', String(index + 1).padStart(2, '0')), element('h3', '', localized(topic.title)), element('p', '', localized(topic.detail)), action);
    grid.append(card);
  });

  document.querySelector('#featured-sources').replaceChildren(sourceCard(sources.geostat), sourceCard(sources.nbg));
  document.querySelector('#source-list').replaceChildren(...Object.values(sources).map(sourceCard));
  document.querySelector('#current-page').textContent = selectedTopic ? localized(selectedTopic.title) : text(page);
  document.querySelectorAll('[data-page]').forEach((section) => {
    section.hidden = section.dataset.page !== (selectedTopic ? 'topic' : page);
  });
  if (selectedTopic) {
    document.querySelector('#topic-title').textContent = localized(selectedTopic.title);
    document.querySelector('#topic-number').textContent = `${String(topics.indexOf(selectedTopic) + 1).padStart(2, '0')} / ${topics.length}`;
    document.querySelector('#topic-detail').textContent = localized(selectedTopic.detail);
    const topicSources = document.querySelector('#topic-sources');
    topicSources.replaceChildren(...selectedTopic.sources.map((key) => sourceCard(sources[key])));
    document.querySelector('#source-pending').hidden = selectedTopic.sources.length > 0;
    document.querySelector('#check-sources').hidden = selectedTopic.sources.length === 0;
  }
}

document.querySelectorAll('[data-language]').forEach((button) => {
  button.addEventListener('click', () => {
    language = button.dataset.language;
    render();
  });
});

document.querySelector('#nav-toggle').addEventListener('click', () => {
  categoriesExpanded = !categoriesExpanded;
  render();
});

document.querySelector('.skip-link').addEventListener('click', (event) => {
  event.preventDefault();
  document.querySelector('#main-content').focus();
});

window.addEventListener('hashchange', () => {
  render();
  const visiblePage = document.querySelector('.portal-page:not([hidden])');
  visiblePage.querySelector('[data-page-heading]').focus();
});

render();
