from edc_constants.constants import YES
from edc_metadata import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, P, register

app_label = 'study_subject'


@register()
class EducationRuleGroup(CrfRuleGroup):
    employment = CrfRule(
        predicate=P('employment', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=f'{app_label}.community_engagement'
    )

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.education'
