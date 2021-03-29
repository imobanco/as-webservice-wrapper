from zeep.xsd.valueobjects import CompoundValue


class ProcessedResponse:
    def __init__(self, response):
        self._response = response
        self.data = None
        self._create_data()

    @property
    def original_data(self):
        return self._response

    def _create_data(self):
        if isinstance(self._response, list):
            self._create_list_data()
        elif isinstance(self._response, CompoundValue):
            self._create_entry_data(self._response)

    def _create_list_data(self):
        data = []
        for item in self._response:
            data.append(
                self._create_entry_data(item, False)
            )
        self.data = data

    def _create_entry_data(self, entry, set_data=True):
        data = entry.__dict__['__values__']
        if set_data:
            self.data = data
        return data
