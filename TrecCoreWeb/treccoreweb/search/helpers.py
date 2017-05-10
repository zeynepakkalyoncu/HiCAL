from treccoreweb.judgment.models import Judgement


def join_judgments(document_values, document_ids, user, topic):
    """
    Adds the relevance judgment of the document to the document_values dict.
    If document has not been judged yet, `isJudged` will be False.
    :param user:
    :param topic:
    :param document_values:
    :param document_ids:
    :return: document_values with extra information about the document
    """

    judged_docs = Judgement.objects.filter(user=user,
                                           topic=topic,
                                           doc_id__in=document_ids)
    judged_docs = {j.doc_id: j for j in judged_docs}

    for key in document_values:
        isJudged = True if key in judged_docs else False
        if isJudged:
            judgedment = judged_docs.get(key)
            document_values[key]['relevance_judgment'] = {
                "relevant": judgedment.relevant,
                "nonrelevant": judgedment.nonrelevant,
                "notsure": judgedment.notsure,
            }
        document_values[key]['isJudged'] = isJudged
    return document_values
