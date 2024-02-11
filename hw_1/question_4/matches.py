__author__="Andrew Serra"

from copy import deepcopy

def stable_matching(choosers: list[str], opts: list[str]) -> dict[str, str]:
    '''
    Runs the stable matching algorithm by Gale-Shapley. Returns the matching result
    @param choosers A list of preferences of the proposers
    @param opts A list of preferences of the acceptors

    @returns Pairing result as a dictionary mapping
    '''
    matches_c = dict.fromkeys(choosers[0])
    matches_o = dict.fromkeys(opts[0])
    unmatched_count = len(choosers)
    curr_chooser_idx = 0
    chooser_st = deepcopy(choosers)

    while unmatched_count:
        if matches_c[str(curr_chooser_idx)] is None:
            # Remove the highest preferred
            # it will get matched if possible, or rejected
            # no longer needed
            top_pref = chooser_st[curr_chooser_idx].pop(0)
            
            if matches_o[top_pref] is None:
                matches_c[str(curr_chooser_idx)] = top_pref
                matches_o[top_pref] = str(curr_chooser_idx)
                unmatched_count -= 1
            else:
                # Less than, because the index which is lower means higher preference
                if opts[int(top_pref)].index(str(curr_chooser_idx)) < opts[int(top_pref)].index(matches_o[top_pref]):
                    matches_c[matches_o[top_pref]] = None
                    matches_c[str(curr_chooser_idx)] = top_pref
                    matches_o[top_pref] = str(curr_chooser_idx)

        curr_chooser_idx = (curr_chooser_idx + 1) % len(choosers)

    return matches_c

def check_unique_stable_matching(choosers: list[str], opts: list[str]) -> bool:
    '''
    Runs two sided for stable matching to see if the pairing is
    fully unique.
    @param choosers A list of preferences of the proposers
    @param opts A list of preferences of the acceptors

    @returns True if the matching is unique, else False
    '''
    # Run two different requester and acceptor pairing
    _sm_p1 = stable_matching(choosers, opts)
    _sm_p2 = stable_matching(opts, choosers)

    # Identify if there are same matches
    for key in _sm_p1.keys():
        if _sm_p1[key] == _sm_p2[key]:
            return False
        
    return True


if __name__ == "__main__":
    pref_size = int(input())

    choosers = [input().strip().split() for _ in range(pref_size)]
    options = [input().strip().split() for _ in range(pref_size)]

    print("YES" if check_unique_stable_matching(choosers, options) else "NO")
