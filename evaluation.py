import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    return set(ent.text.lower() for ent in doc.ents)

def entity_precision(predicted, reference):
    pred_ents = extract_entities(predicted)
    ref_ents = extract_entities(reference)

    if len(pred_ents) == 0:
        return 0

    precision = len(pred_ents & ref_ents) / len(pred_ents)
    hallucination_rate = 1 - precision

    return precision, hallucination_rate