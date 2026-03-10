class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None or self.props == "":
            return ""
        else:
            prop_string = ""
            for prop in self.props:
                prop_string += f' {prop}="{self.props[prop]}"'

            return prop_string

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        else:
            o_tag = f"<{self.tag}{self.props_to_html()}>"
            c_tag = f"</{self.tag}>"

            return o_tag + self.value + c_tag
