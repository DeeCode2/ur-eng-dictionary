from csv_search import db_search

def test_search_phrase() -> None:
    """Test that db_search returns the matching definitions when given an english phrase."""
    assert db_search("sword") == {'specific': [['abẹrẹn', 'n.', 'sword']], 'non_specific': []}