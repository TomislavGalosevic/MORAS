Require Import Classical.

Goal forall X Y : Prop, (X /\ ~Y) \/ (~X /\ ~Y) \/ (~X /\ Y) <-> ~Y \/ ~X.
Proof.
 intros. split. intros H.
 -destruct H as [H1 | [H2|H3]].
  -- destruct H1 as [_ ny]. left. exact ny.
  -- destruct H2 as [nx _]. right. exact nx.
  -- destruct H3 as [nx _]. right. exact nx.
 - intros. destruct (classic Y) as [y | ny].
   -- right. right. split.
     --- intros x. destruct H as [ny | nx].
       ---- apply ny. exact y.
       ---- apply nx. exact x.
     --- exact y.
   -- destruct (classic X) as [x | nx].
    --- left. split.
      ---- exact x.
      ---- exact ny.
    --- right. left. split.
      ---- exact nx.
      ---- exact ny.
Qed.
