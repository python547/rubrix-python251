from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.text_classification_search_aggregations_metadata_additional_property import (
    TextClassificationSearchAggregationsMetadataAdditionalProperty,
)

T = TypeVar("T", bound="TextClassificationSearchAggregationsMetadata")


@attr.s(auto_attribs=True)
class TextClassificationSearchAggregationsMetadata:
    """ """

    additional_properties: Dict[
        str, TextClassificationSearchAggregationsMetadataAdditionalProperty
    ] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text_classification_search_aggregations_metadata = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = TextClassificationSearchAggregationsMetadataAdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        text_classification_search_aggregations_metadata.additional_properties = (
            additional_properties
        )
        return text_classification_search_aggregations_metadata

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> TextClassificationSearchAggregationsMetadataAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: TextClassificationSearchAggregationsMetadataAdditionalProperty,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
