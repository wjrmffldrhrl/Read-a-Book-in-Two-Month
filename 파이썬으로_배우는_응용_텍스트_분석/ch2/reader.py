# 원시 HTML 문서들을 전처리하기 위한 말뭉치 리더
class HTMLCorpusReader(CategorizedCorpusReader, CorpusReader):


    # 말뭉치 리더 초기화
    def __init__(self, root, fileids=DOC_PATTERN, encoding='utf8',
                 tags=TAGS, **kwargs):

        # 기본 카테고리 패턴이 클래스로 전달되지 않는다면 기본 카테고리 패턴을 추가한다.
        if not any(key.startswith('cat_') for key in kwargs.keys()):
            kwargs['cat_pattern'] = CAT_PATTERN

        # NLTK 말뭉치 리더 객체들을 초기화한다.
        CategorizedCorpusReader.__init__(self, kwargs)
        CorpusReader.__init__(self, root, fileids, encoding)

        # 특별히 추출하기를 바라는 태그들을 저장한다.
        self.tags = tags

    
    # 각 내부 말뭉치 리더 기능으로 전달되는 항목에 따라
    # fileid 또는 범주의 목록을 반환한다.
    # NLTK의 'CategorizedPlaintextCorpusReader'와 유사하게 구현된다.
    def resolve(self, fileids, categories):
    
        # 예외 발생
        if fileids is not None and categories is not None:
            raise ValueError("Specify fileids or categories, not both")

        if categories is not None:
            return self.fileids(categories)

        return fileids

    # HTMl 문서의 전체 텍스트를 반환하고, 문서를 읽고 난 후에는 문서를 닫고
    # 메모리에 안전한 방식으로 저장한다.
    def docs(self, fileids=None, categories=None):
       
        # fileid들과 범주들을 분해한다.
        fileids = self.resolve(fileids, categories)

        # 생성기를 만들어 한 번에 1개 문서를 메모리에 적재한다.
        for path, encoding in self.abspaths(fileids, include_encoding=True):
            with codecs.open(path, 'r', encoding=encoding) as f:
                yield f.read()


    # 파일의 튜플, 팡리 식별자 및 디스크의 크기 목록을 반환한다.
    # 이 함수는 말뭉치 중에 유별나게 큰 파일을 탐지하는 데 사용된다.
    def sizes(self, fileids=None, categories=None):
     
        # 필드와 범주 분해
        fileids = self.resolve(fileids, categories)

        # 생성기를 만들고, 모든 경로를 얻고 파일 크기를 계산한다.
        for path in self.abspaths(fileids):
            yield os.path.getsize(path)


    
    # 각 문서의 HTML 내용을 반환하고, readability-lxml 라이브러리를 사용해 정제한다.
    def html(self, fileids=None, categories=None):

        for doc in self.docs(fileids, categories):
            try:
                yield Paper(doc).summary()
            except Unparseable as e:
                print("Could not parse HTML : {}".format(e))
                continue


    # BeautifulSoup를 사용해 HTML에서 단락들을 대상으로 구문 분석을 한다.
    def pasre(self, fileids=None, categories=None):
        for html in self.html(fileids, categories):
            soup = bs4.Beautifulsoup(html, 'lxml')
            for element in soup.find_all(tags):
                yield element.text
            soup.decompose()


    # 내장된 문장 토크나이저를 사용해 단락에서 문장을 추출한다.
    # 이 메서드는 BeautifulSoup를 사용해 HTML을 대상으로 구문분석을 하는 parse 메서드를 사용한다.
    def sents(self, fileids=None, categories=None):
        for paragraph in self.paras(fileids, categories):
            for sentence in sent_tokenize(paragraph):
                yield sentence

    def words(self, fileids=None, categories=None):
    for sentence in self.sents(fileids, categories):
        for token in wordpunct_tokenize(sentence):
            yield token

    def tokenize(self, fileids=None, categories=None):
    for paragraph in self,paras(fileids=fileids):
        yield [
               pos_tag(wordpunct_tokenize(sent))
               for sent in sent_tokenize(paragraph)
        ]

    def describe(self, fileids=None, categories=None):
    started = time.time()

    counts = nltk.FreqDist()
    tokens = nltk.FreqDist()

    for para in self.paras(filleids, categories):
        counts['paras'] += 1

        for sent in para:
            counts['sents'] += 1

            for word, tag in sent:
                coutns['words'] += 1
                tokens[word] += 1

    
    n_fileids = len(self.resolve(fileids, categories) or self.fileids())
    n_topics = len(self.categories(self.resolve(fileids, categories)))

    return {
        'files': n_fileids,
        'topics': n_topics,
        'paras': counts['paras'],
        'sents': counts['sents'],
        'words': counts['words'],
        'vocab': len(tokens),
        'lexdiv': float(counts['words']) / float(len(tokens)),
        'ppdoc': float(counts['paras']) / float(n_fileids),
        'sppar': float(counts['sents']) / float(counts['paras']),
        'secs': time.time() - started,
    }