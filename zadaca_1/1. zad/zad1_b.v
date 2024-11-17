Require Import Classical.

Goal forall X Y Z : Prop, (~(~X /\ Y /\ Z) /\ ~(X /\ Y /\ ~Z) /\ (X /\ ~Y /\ Z)) <-> (X /\ ~Y /\ Z).
 intros. split. intros H.
 destruct H as [H1 [H2 [x [ny z]]]].
 - split.
  -- exact x.
  -- split.
    --- exact ny.
    --- exact z.
 - intros H. destruct H as [x[ny z]]. split.
   -- intros [nx[y _]]. contradiction.
   -- split.
    --- intros [_ [y nz]]. contradiction.
    --- split.
      ---- exact x.
      ---- split.
         ----- exact ny.
         ----- exact z.
Qed.